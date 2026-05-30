from decimal import Decimal

from django.db import models


class DishBase(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image_url = models.URLField()

    class Meta:
        abstract = True
        ordering = ["name"]

    def __str__(self):
        return self.name


class Appetizers(DishBase):
    pass


class Salads(DishBase):
    pass


class Soups(DishBase):
    pass


class Pasta(DishBase):
    pass


class Pizza(DishBase):
    pass


class Seafood(DishBase):
    pass


class Steaks(DishBase):
    pass


class Burgers(DishBase):
    pass


class Sandwiches(DishBase):
    pass


class Vegetarian(DishBase):
    pass


class Vegan(DishBase):
    pass


class GlutenFree(DishBase):
    pass


class Desserts(DishBase):
    pass


class Beverages(DishBase):
    pass


class Cocktails(DishBase):
    pass


class Breakfast(DishBase):
    pass


class Brunch(DishBase):
    pass


class KidsMenu(DishBase):
    pass


class Sides(DishBase):
    pass


class Specials(DishBase):
    pass


class Order(models.Model):
    id = models.AutoField(primary_key=True)
    PAYMENT_CASH = "cash"
    PAYMENT_CARD = "card"
    PAYMENT_TRANSFER = "transfer"
    PAYMENT_EASYPAISA = "easypaisa"

    PAYMENT_METHOD_CHOICES = [
        (PAYMENT_CASH, "Cash on Delivery"),
        (PAYMENT_CARD, "Card on Delivery"),
        (PAYMENT_TRANSFER, "Bank Transfer"),
        (PAYMENT_EASYPAISA, "EasyPaisa"),
    ]

    STATUS_PENDING = "pending"
    STATUS_CONFIRMED = "confirmed"
    STATUS_PREPARING = "preparing"
    STATUS_COMPLETED = "completed"
    STATUS_CANCELLED = "cancelled"

    STATUS_CHOICES = [
        (STATUS_PENDING, "Pending"),
        (STATUS_CONFIRMED, "Confirmed"),
        (STATUS_PREPARING, "Preparing"),
        (STATUS_COMPLETED, "Completed"),
        (STATUS_CANCELLED, "Cancelled"),
    ]

    full_name = models.CharField(max_length=120)
    phone = models.CharField(max_length=30)
    email = models.EmailField(blank=True)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    notes = models.TextField(blank=True)
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHOD_CHOICES)
    payment_reference = models.CharField(max_length=120, blank=True)
    payment_status = models.CharField(max_length=20, default=STATUS_PENDING)
    order_status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=STATUS_PENDING)
    subtotal = models.DecimalField(max_digits=8, decimal_places=2, default=Decimal("0.00"))
    delivery_fee = models.DecimalField(max_digits=8, decimal_places=2, default=Decimal("0.00"))
    total = models.DecimalField(max_digits=8, decimal_places=2, default=Decimal("0.00"))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"Order #{self.pk} - {self.full_name}"


class OrderItem(models.Model):
    id = models.AutoField(primary_key=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="items")
    category = models.CharField(max_length=100)
    dish_name = models.CharField(max_length=120)
    quantity = models.PositiveIntegerField(default=1)
    unit_price = models.DecimalField(max_digits=8, decimal_places=2)
    line_total = models.DecimalField(max_digits=8, decimal_places=2)
    image_url = models.URLField(blank=True)
    source_model = models.CharField(max_length=100, blank=True)
    source_object_id = models.PositiveIntegerField(null=True, blank=True)

    class Meta:
        ordering = ["id"]

    def __str__(self):
        return f"{self.dish_name} x{self.quantity}"
