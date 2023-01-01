from django import forms
from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ['user']

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'user_phone_number': 'Phone Number',
            'user_zip': 'ZIP',
            'user_city': 'City',
            'user_address_line_1': 'Address line 1',
            'user_address_line_2': 'Address line 2',
            'user_state': 'State',
        }

        self.fields['user_phone_number'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'user_country':
                if self.fields[field]:
                    placeholder = f'{placeholders[field]}'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].label = False
