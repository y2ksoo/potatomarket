from django import forms
from . import models


class SearchForm(forms.Form):
    city = forms.CharField(initial="모든지역", required=False)
    name = forms.CharField(required=False)
    price = forms.IntegerField(required=False)
    category = forms.ModelMultipleChoiceField(
        required=False,
        queryset=models.Category.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )

class WareForm(forms.ModelForm):
    class Meta:
        model = models.Ware
        fields = ['name', 'description', 'price', 'city', 'category', 'photo'] 
        widgets = {
            'description': forms.Textarea(attrs={"rows":10, "cols":20}),
            'category': forms.CheckboxSelectMultiple(),
        }

    # def save(self, *args, **kwargs):        
    #     ware = super().save(commit=False) # Call the real save() method
    #     print(self)
    #     print(args)

    #     ware.save()
