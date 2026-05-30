from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("ab/", views.about),
    path("menu/", views.menu, name="menu"),
    path("cart/", views.cart, name="cart"),
    path("checkout/", views.checkout, name="checkout"),
    path("order/<int:order_id>/success/", views.order_success, name="order_success"),
    path("cart/add/<str:category_key>/<int:item_id>/", views.add_to_cart, name="add_to_cart"),
    path("cart/update/<str:line_key>/", views.update_cart_item, name="update_cart_item"),
    path("cart/remove/<str:line_key>/", views.remove_cart_item, name="remove_cart_item"),
    path("dashboard/login/", views.dashboard_login, name="dashboard_login"),
    path("dashboard/logout/", views.dashboard_logout, name="dashboard_logout"),
    path("dashboard/", views.dashboard_home, name="dashboard_home"),
    path("dashboard/<str:category_key>/", views.dashboard_category, name="dashboard_category"),
    path("dashboard/<str:category_key>/new/", views.dashboard_dish_create, name="dashboard_dish_create"),
    path(
        "dashboard/<str:category_key>/<int:item_id>/edit/",
        views.dashboard_dish_edit,
        name="dashboard_dish_edit",
    ),
    path(
        "dashboard/<str:category_key>/<int:item_id>/delete/",
        views.dashboard_dish_delete,
        name="dashboard_dish_delete",
    ),
]
