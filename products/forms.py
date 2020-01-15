from django import forms
from products.models import *


class AdvertForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = ["tracker", "name", "price", "description", "img", "user"]        
