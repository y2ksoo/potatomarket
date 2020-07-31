from django import forms
from . import models


class WareForm(forms.ModelForm):
    class Meta:
        model = models.Ware
        fields = ['name', 'description', 'price', 'city', 'seller', 'category'] 
        widgets = {
            'category': forms.CheckboxSelectMultiple(),
        }

    def save(self, *args, **kwargs):
        ware = super().save(*args, **kwargs) # Call the real save() method
        ware.save()
