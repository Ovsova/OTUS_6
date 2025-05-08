from django import forms
from .models import Product, Category
from django.core.exceptions import ValidationError

BAD_WORDS = ['биба', 'буба', 'быба', 'боба']


class ProductModelForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'category']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
        }

    def clean_name(self):
        name = self.cleaned_data['name']
        if len(name) < 10:
            raise ValidationError('Название должно быть более 10 символов')
        return name

    def clean(self):
        cleaned_data = super().clean()
        description = cleaned_data.get('description')
        if description:
            for word in BAD_WORDS:
                if word in description.lower():
                    raise ValidationError(f'Слово {word} нельзя использовать')


class CategoryModelForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),

        }

    def clean_name(self):
        name = self.cleaned_data['name']
        if len(name) < 3:
            raise ValidationError('Название должно быть более 3 символов')
        return name

    def clean(self):
        cleaned_data = super().clean()
        description = cleaned_data.get('description')
        if description:
            for word in BAD_WORDS:
                if word in description.lower():
                    raise ValidationError(f'Слово {word} нельзя использовать')
