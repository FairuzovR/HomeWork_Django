from django.forms import ModelForm
from catalog.models import Product
from django.forms.fields import BooleanField
from django.core.exceptions import ValidationError

error_worlds = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']

class StyleForMexin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for fild_name, fild in self.fields.items():
            if isinstance(fild, BooleanField):
                fild.widget.attrs['class'] = 'form-check-input'
            else:
                fild.widget.attrs['class'] = 'form-control'

class ProductForm(StyleForMexin, ModelForm):
    class Meta:
        model = Product
        exclude = "__all__"

    def clean_name(self):
        name = self.cleaned_data['name']
        for error_world in error_worlds:
            if error_world in name.lower():
                raise ValidationError(f'{error_world} не должно находиться в названии')

        return name

    def clean_description(self):
        description = self.cleaned_data['description']
        for error_world in error_worlds:
            if error_world in description.lower():
                raise ValidationError(f'{error_world} не должно находиться в описании')

        return description

