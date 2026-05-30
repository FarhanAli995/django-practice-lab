from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Appetizers, Order


class CartAndCheckoutTests(TestCase):
    def setUp(self):
        self.dish = Appetizers.objects.create(
            name="Test Kebab",
            description="Smoky and spiced.",
            price="450.00",
            image_url="https://example.com/kebab.jpg",
        )

    def test_add_to_cart_and_checkout_creates_order(self):
        add_response = self.client.post(reverse("add_to_cart", args=["appetizers", self.dish.id]), {"quantity": 2})
        self.assertEqual(add_response.status_code, 302)

        checkout_response = self.client.post(
            reverse("checkout"),
            {
                "full_name": "Ali Khan",
                "phone": "03001234567",
                "email": "ali@example.com",
                "address": "Street 1",
                "city": "Rawalpindi",
                "payment_method": "cash",
                "payment_reference": "",
                "notes": "Extra chutney",
            },
        )

        self.assertEqual(checkout_response.status_code, 302)
        self.assertEqual(Order.objects.count(), 1)
        order = Order.objects.get()
        self.assertEqual(order.items.count(), 1)
        self.assertEqual(order.items.first().quantity, 2)


class DashboardTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="manager",
            password="StrongPass123",
            is_staff=True,
        )

    def test_dashboard_requires_login(self):
        response = self.client.get(reverse("dashboard_home"))
        self.assertEqual(response.status_code, 302)

    def test_dashboard_category_available_for_staff(self):
        self.client.login(username="manager", password="StrongPass123")
        response = self.client.get(reverse("dashboard_category", args=["appetizers"]))
        self.assertEqual(response.status_code, 200)
