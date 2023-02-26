# To modify the checkbox input on our book form
# https://github.com/django/django/blob/main/django/forms/widgets.py

# https://github.com/django/django/blob/main/django/forms/templates/django/forms/widgets/clearable_file_input.html


from django.forms.widgets import ClearableFileInput
from django.utils.translation import gettext_lazy as _


class CustomClearableFileInput(ClearableFileInput):
    clear_checkbox_label = _('Remove')
    initial_text = _('Current Image')
    input_text = _('')
    template_name = (
        'books/custom_widgets_templates/custom_clearable_file_input.html')
