from django import forms
from .models import Fertilizer,Medicine
class InquiryForm(forms.Form):
    product = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Product', 'readonly': 'readonly'}))
    quantity = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control','required':'required', 'placeholder': 'Quantity'}))
    phoneno = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','required':'required', 'placeholder': 'Phone'}))
    fertilizer_package = forms.ModelChoiceField(
        queryset=Fertilizer.objects.all(),
        empty_label="Select Fertilizer",
        widget=forms.Select(attrs={"class": "form-control"}),
        required=False
    )

    medicine_package = forms.ModelChoiceField(
        queryset=Medicine.objects.all(),
        empty_label="Select Medicine",
        widget=forms.Select(attrs={"class": "form-control"}),
        required=False
    )
    package = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','required':'required', 'placeholder': 'Package'}))
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','required':'required', 'placeholder': 'Name'}))
    comment = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control','required':'required', 'placeholder': 'Message'}))
