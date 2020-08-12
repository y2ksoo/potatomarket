from django import forms
from . import models


class SearchForm(forms.Form):
    city = forms.CharField(initial="모든지역")
    name = forms.CharField(required=False)
    price = forms.IntegerField(required=False)
    # seller = forms.CharField(required=False)
    category = forms.ModelMultipleChoiceField(
        required=False,
        queryset=models.Category.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )

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
