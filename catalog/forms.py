from django.forms import ModelForm
from catalog.models import Product
from django.forms.fields import BooleanField
from django.core.exceptions import ValidationError

error_world = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']

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
        name_split = name.split()
        for name_world in name_split:
            if name_world.lower() in error_world:
                raise ValidationError(f'{name_world} не должно находиться в названии')

        return name

    def clean_description(self):
        description = self.cleaned_data['description']
        description_split = description.split()
        for description_world in description_split:
            if description_world.lower() in error_world:
                raise ValidationError(f'{description_world} не должно находиться в описании')

        return description

