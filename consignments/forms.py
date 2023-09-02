from django import forms
from products.widgets import CustomClearableFileInput
from .models import Consignment


class ConsignmentForm(forms.ModelForm):

    class Meta:
        model = Consignment
        fields = 'name', 'description', 'image_1',

    image_1 = forms.ImageField(label='Image', required=False, 
                                widget=CustomClearableFileInput)
