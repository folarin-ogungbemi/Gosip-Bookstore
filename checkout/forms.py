from django import forms
from checkout.models import Order


class OrderForm(forms.ModelForm):
    full_name = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'John Doe'}))
    email = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'john@doe.com'}))
    phone_number = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': '+49 12345678900'}))
    address_line_1 = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={'placeholder': 'No.5, John primary street'}))
    address_line_2 = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={'placeholder': 'No.5, John secondary street'}))
    zip = forms.CharField(
        label='ZIP',
        required=False,)
    city = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Berlin'}))
    state = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Berlin'}))

    class Meta:
        model = Order
        fields = [
            'full_name',
            'email',
            'phone_number',
            'address_line_1',
            'address_line_2',
            'zip',
            'city',
            'state',
            'country',]
