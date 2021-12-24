from django import forms

from . models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name','tag', 'image' , 'category', 'description']
        widgets = {
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'tag': forms.Select(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
        }
