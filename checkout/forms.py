from django import forms
from checkout.models import Order


class OrderForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = [
            'first_name',
            'last_name',
            'email',
            'phone_number',
            'house_number',
            'street',
            'postal_address',
            'city',
            'country',]
