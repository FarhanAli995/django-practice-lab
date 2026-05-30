from decimal import Decimal

from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.db import transaction
from django.db.utils import OperationalError, ProgrammingError
from django.http import Http404
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from .forms import CheckoutForm, DashboardAuthenticationForm, build_dish_form
from .models import (
    Appetizers,
    Beverages,
    Breakfast,
    Brunch,
    Burgers,
    Cocktails,
    Desserts,
    GlutenFree,
    KidsMenu,
    Order,
    OrderItem,
    Pasta,
    Pizza,
    Salads,
    Sandwiches,
    Seafood,
    Sides,
    Soups,
    Specials,
    Steaks,
    Vegan,
    Vegetarian,
)


def _staff_required(user):
    return user.is_authenticated and user.is_staff


staff_required = user_passes_test(_staff_required, login_url="dashboard_login")

MENU_MODELS = [
    {"title": "Appetizers", "key": "appetizers", "model": Appetizers},
    {"title": "Salads", "key": "salads", "model": Salads},
    {"title": "Soups", "key": "soups", "model": Soups},
    {"title": "Pasta", "key": "pasta", "model": Pasta},
    {"title": "Pizza", "key": "pizza", "model": Pizza},
    {"title": "Seafood", "key": "seafood", "model": Seafood},
    {"title": "Steaks", "key": "steaks", "model": Steaks},
    {"title": "Burgers", "key": "burgers", "model": Burgers},
    {"title": "Sandwiches", "key": "sandwiches", "model": Sandwiches},
    {"title": "Vegetarian", "key": "vegetarian", "model": Vegetarian},
    {"title": "Vegan", "key": "vegan", "model": Vegan},
    {"title": "Gluten Free", "key": "glutenfree", "model": GlutenFree},
    {"title": "Desserts", "key": "desserts", "model": Desserts},
    {"title": "Beverages", "key": "beverages", "model": Beverages},
    {"title": "Cocktails", "key": "cocktails", "model": Cocktails},
    {"title": "Breakfast", "key": "breakfast", "model": Breakfast},
    {"title": "Brunch", "key": "brunch", "model": Brunch},
    {"title": "Kids Menu", "key": "kidsmenu", "model": KidsMenu},
    {"title": "Sides", "key": "sides", "model": Sides},
    {"title": "Specials", "key": "specials", "model": Specials},
]
MENU_MODEL_MAP = {entry["key"]: entry for entry in MENU_MODELS}
CART_SESSION_KEY = "restaurant_cart"
DEFAULT_DELIVERY_FEE = Decimal("250.00")


def _featured_dishes():
    return [
        {
            "name": "Chicken_Biryani",
            "description": "Traditional Pakistani spicy rice dish cooked with tender chicken and aromatic spices.",
            "price": "$12",
        },
        {
            "name": "Beef Karahi",
            "description": "Rich and flavorful beef cooked with tomatoes, garlic, and traditional spices.",
            "price": "$15",
        },
        {
            "name": "Chicken Tikka",
            "description": "Juicy grilled chicken marinated with yogurt and traditional BBQ spices.",
            "price": "$10",
        },
        {
            "name": "Seekh Kebab",
            "description": "Minced meat kebabs grilled on charcoal with authentic desi flavor.",
            "price": "$9",
        },
        {
            "name": "Butter Chicken",
            "description": "Creamy tomato curry cooked with soft chicken and rich butter flavor.",
            "price": "$13",
        },
        {
            "name": "Chapli Kebab",
            "description": "Famous Peshawari style kebab made with minced beef and special spices.",
            "price": "$11",
        },
    ]


def _menu_item_payload(item, section):
    return {
        "id": item.pk,
        "name": item.name,
        "description": item.description,
        "price": item.price,
        "image_url": item.image_url,
        "category_key": section["key"],
        "category_title": section["title"],
    }


def _cart_dict(request):
    return request.session.setdefault(CART_SESSION_KEY, {})


def _cart_items(request):
    cart = _cart_dict(request)
    items = []
    subtotal = Decimal("0.00")

    for item in cart.values():
        quantity = int(item["quantity"])
        unit_price = Decimal(item["price"])
        line_total = unit_price * quantity
        subtotal += line_total
        items.append(
            {
                **item,
                "quantity": quantity,
                "unit_price": unit_price,
                "line_total": line_total,
            }
        )

    return items, subtotal


def _cart_count(request):
    cart = _cart_dict(request)
    return sum(int(item["quantity"]) for item in cart.values())


def _cart_context(request):
    items, subtotal = _cart_items(request)
    delivery_fee = DEFAULT_DELIVERY_FEE if items else Decimal("0.00")
    total = subtotal + delivery_fee
    return {
        "cart_items": items,
        "cart_count": sum(item["quantity"] for item in items),
        "cart_subtotal": subtotal,
        "cart_delivery_fee": delivery_fee,
        "cart_total": total,
    }


def _load_menu_sections():
    menu_sections = []
    total_items = 0
    database_ready = True

    try:
        for section in MENU_MODELS:
            model = section["model"]
            objects = list(model.objects.all())
            items = [_menu_item_payload(item, section) for item in objects]
            total_items += len(items)
            menu_sections.append({**section, "items": items, "count": len(items)})
    except (OperationalError, ProgrammingError):
        database_ready = False
        menu_sections = [{**section, "items": [], "count": 0} for section in MENU_MODELS]

    return {
        "menu_sections": menu_sections,
        "total_categories": len(menu_sections),
        "total_items": total_items,
        "database_ready": database_ready,
    }


def home(request):
    context = {
        "featured_dishes": _featured_dishes(),
        "stats": [
            {"value": "12+", "label": "Signature dishes"},
            {"value": "20", "label": "Menu categories"},
            {"value": "4.8/5", "label": "Guest rating"},
        ],
        "highlights": [
            "Slow-cooked curries and charcoal-grilled specialties",
            "Fresh ingredients sourced daily for every service",
            "Family-friendly dining with classic Pakistani comfort food",
        ],
        **_cart_context(request),
    }
    return render(request, "core/home.html", context)


def about(request):
    return render(request, "core/about.html", _cart_context(request))


def menu(request):
    context = {
        **_load_menu_sections(),
        **_cart_context(request),
    }
    return render(request, "core/menu.html", context)


def cart(request):
    return render(request, "core/cart.html", _cart_context(request))


@require_POST
def add_to_cart(request, category_key, item_id):
    section = MENU_MODEL_MAP.get(category_key)
    if not section:
        raise Http404("Invalid category.")

    item = get_object_or_404(section["model"], pk=item_id)
    quantity = max(int(request.POST.get("quantity", 1) or 1), 1)
    cart = _cart_dict(request)
    line_key = f"{category_key}:{item_id}"

    if line_key in cart:
        cart[line_key]["quantity"] = int(cart[line_key]["quantity"]) + quantity
    else:
        cart[line_key] = {
            "line_key": line_key,
            "item_id": item_id,
            "category_key": category_key,
            "category_title": section["title"],
            "name": item.name,
            "price": str(item.price),
            "image_url": item.image_url,
            "quantity": quantity,
            "model_name": section["model"].__name__,
        }

    request.session.modified = True
    messages.success(request, f"{item.name} added to cart.")
    return redirect(request.POST.get("next") or "menu")


@require_POST
def update_cart_item(request, line_key):
    cart = _cart_dict(request)
    if line_key in cart:
        quantity = max(int(request.POST.get("quantity", 1) or 1), 0)
        if quantity == 0:
            cart.pop(line_key, None)
        else:
            cart[line_key]["quantity"] = quantity
        request.session.modified = True
    return redirect("cart")


@require_POST
def remove_cart_item(request, line_key):
    cart = _cart_dict(request)
    cart.pop(line_key, None)
    request.session.modified = True
    messages.info(request, "Item removed from cart.")
    return redirect("cart")


def checkout(request):
    cart_context = _cart_context(request)
    if not cart_context["cart_items"]:
        messages.info(request, "Your cart is empty.")
        return redirect("menu")

    if request.method == "POST":
        form = CheckoutForm(request.POST)
        if form.is_valid():
            with transaction.atomic():
                order = form.save(commit=False)
                order.subtotal = cart_context["cart_subtotal"]
                order.delivery_fee = cart_context["cart_delivery_fee"]
                order.total = cart_context["cart_total"]
                order.payment_status = (
                    Order.STATUS_PENDING
                    if order.payment_method in {Order.PAYMENT_TRANSFER, Order.PAYMENT_EASYPAISA}
                    else Order.STATUS_CONFIRMED
                )
                order.save()

                for item in cart_context["cart_items"]:
                    OrderItem.objects.create(
                        order=order,
                        category=item["category_title"],
                        dish_name=item["name"],
                        quantity=item["quantity"],
                        unit_price=item["unit_price"],
                        line_total=item["line_total"],
                        image_url=item["image_url"],
                        source_model=item["model_name"],
                        source_object_id=item["item_id"],
                    )

            request.session[CART_SESSION_KEY] = {}
            request.session.modified = True
            return redirect("order_success", order_id=order.pk)
    else:
        form = CheckoutForm()

    return render(
        request,
        "core/checkout.html",
        {
            "form": form,
            **cart_context,
        },
    )


def order_success(request, order_id):
    order = get_object_or_404(Order.objects.prefetch_related("items"), pk=order_id)
    return render(request, "core/order_success.html", {"order": order, **_cart_context(request)})


def dashboard_login(request):
    if request.user.is_authenticated and request.user.is_staff:
        return redirect("dashboard_home")

    form = DashboardAuthenticationForm(request, data=request.POST or None)
    if request.method == "POST" and form.is_valid():
        login(request, form.get_user())
        return redirect(request.GET.get("next") or "dashboard_home")

    return render(request, "core/dashboard/login.html", {"form": form})


@login_required
def dashboard_logout(request):
    logout(request)
    return redirect("dashboard_login")


@staff_required
def dashboard_home(request):
    sections = []
    total_dishes = 0
    for section in MENU_MODELS:
        count = section["model"].objects.count()
        total_dishes += count
        sections.append({**section, "count": count})

    recent_orders = Order.objects.prefetch_related("items")[:8]
    return render(
        request,
        "core/dashboard/home.html",
        {
            "sections": sections,
            "total_dishes": total_dishes,
            "total_categories": len(sections),
            "order_count": Order.objects.count(),
            "recent_orders": recent_orders,
        },
    )


def _dashboard_section(category_key):
    section = MENU_MODEL_MAP.get(category_key)
    if not section:
        raise Http404("Unknown category.")
    return section


@staff_required
def dashboard_category(request, category_key):
    section = _dashboard_section(category_key)
    dishes = section["model"].objects.all()
    return render(
        request,
        "core/dashboard/category.html",
        {
            "section": section,
            "dishes": dishes,
        },
    )


@staff_required
def dashboard_dish_create(request, category_key):
    section = _dashboard_section(category_key)
    form_class = build_dish_form(section["model"])
    form = form_class(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, f"{section['title']} item created.")
        return redirect("dashboard_category", category_key=category_key)

    return render(
        request,
        "core/dashboard/dish_form.html",
        {
            "section": section,
            "form": form,
            "page_title": f"Add {section['title']} item",
            "submit_label": "Create dish",
        },
    )


@staff_required
def dashboard_dish_edit(request, category_key, item_id):
    section = _dashboard_section(category_key)
    instance = get_object_or_404(section["model"], pk=item_id)
    form_class = build_dish_form(section["model"])
    form = form_class(request.POST or None, instance=instance)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, f"{instance.name} updated.")
        return redirect("dashboard_category", category_key=category_key)

    return render(
        request,
        "core/dashboard/dish_form.html",
        {
            "section": section,
            "form": form,
            "instance": instance,
            "page_title": f"Edit {instance.name}",
            "submit_label": "Save changes",
        },
    )


@staff_required
@require_POST
def dashboard_dish_delete(request, category_key, item_id):
    section = _dashboard_section(category_key)
    instance = get_object_or_404(section["model"], pk=item_id)
    instance.delete()
    messages.info(request, "Dish deleted.")
    return redirect("dashboard_category", category_key=category_key)


def footer(request):
    return render(request, "core/footer.html")
