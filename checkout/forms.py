from django import forms
from checkout.models import Order


class OrderForm(forms.ModelForm):
    first_name = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'John'}))
    last_name = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Doe'}))
    email = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'john@doe.com'}))
    phone_number = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': '+49 12345678900'}))
    house_number = forms.IntegerField(
        required=True,
        widget=forms.TextInput(attrs={'placeholder': '10'}))
    street = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'John street'}))
    postal_address = forms.CharField(
        label='Post Code',
        widget=forms.TextInput(attrs={'required': False}))
    city = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Berlin'}))
    country = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Germany'}))

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
