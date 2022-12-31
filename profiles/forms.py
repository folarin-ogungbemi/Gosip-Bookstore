from django import forms
from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    user_phone_number = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': '+49 12345678900'}))
    user_address_line_1 = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={'placeholder': 'No.5, John primary street'}))
    user_address_line_2 = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={'placeholder': 'No.5, John secondary street'}))
    user_zip = forms.CharField(
        label='ZIP',
        required=False,)
    user_city = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Berlin'}))
    user_state = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Berlin'}))

    class Meta:
        model = UserProfile
        exclude = ['user']
