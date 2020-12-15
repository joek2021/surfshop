from django.forms.widgets import ClearableFileInput
from django.utils.translation import gettext_lazy as _


class CustomClearableFileInput(ClearableFileInput):
    clear_checkbox_label = _('Remove')
    initial_text = ('Current Image')
    input_text = ('')
    template_name = 'products/custom_widget_templates/custom_clearable_input.html'