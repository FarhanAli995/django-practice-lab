from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.forms import modelform_factory

from .models import Order


class DashboardAuthenticationForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "w-full rounded-2xl border border-white/10 bg-stone-900/80 px-4 py-3 text-white outline-none placeholder:text-stone-500",
                "placeholder": "Username",
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "w-full rounded-2xl border border-white/10 bg-stone-900/80 px-4 py-3 text-white outline-none placeholder:text-stone-500",
                "placeholder": "Password",
            }
        )
    )


class CheckoutForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = [
            "full_name",
            "phone",
            "email",
            "address",
            "city",
            "payment_method",
            "payment_reference",
            "notes",
        ]
        widgets = {
            "full_name": forms.TextInput(attrs={"class": "checkout-input", "placeholder": "Full name"}),
            "phone": forms.TextInput(attrs={"class": "checkout-input", "placeholder": "Phone number"}),
            "email": forms.EmailInput(attrs={"class": "checkout-input", "placeholder": "Email address"}),
            "address": forms.TextInput(attrs={"class": "checkout-input", "placeholder": "Street address"}),
            "city": forms.TextInput(attrs={"class": "checkout-input", "placeholder": "City"}),
            "payment_method": forms.Select(attrs={"class": "checkout-input", "id": "payment-method-select"}),
            "payment_reference": forms.TextInput(
                attrs={
                    "class": "checkout-input",
                    "placeholder": "Transaction ID or payment reference",
                    "id": "payment-reference-input",
                }
            ),
            "notes": forms.Textarea(
                attrs={"class": "checkout-input min-h-28", "placeholder": "Order notes", "rows": 4}
            ),
        }

    def clean(self):
        cleaned_data = super().clean()
        payment_method = cleaned_data.get("payment_method")
        payment_reference = (cleaned_data.get("payment_reference") or "").strip()

        if payment_method in {Order.PAYMENT_TRANSFER, Order.PAYMENT_EASYPAISA} and not payment_reference:
            self.add_error("payment_reference", "This payment method requires a transaction reference.")

        if payment_method in {Order.PAYMENT_CASH, Order.PAYMENT_CARD}:
            cleaned_data["payment_reference"] = ""

        return cleaned_data


def build_dish_form(model_class):
    form_class = modelform_factory(
        model_class,
        fields=["name", "description", "price", "image_url"],
        widgets={
            "name": forms.TextInput(attrs={"class": "dashboard-input", "placeholder": "Dish name"}),
            "description": forms.Textarea(
                attrs={
                    "class": "dashboard-input min-h-32",
                    "placeholder": "Dish description",
                    "rows": 5,
                }
            ),
            "price": forms.NumberInput(attrs={"class": "dashboard-input", "step": "0.01", "placeholder": "Price"}),
            "image_url": forms.URLInput(attrs={"class": "dashboard-input", "placeholder": "Image URL"}),
        },
    )
    return form_class
