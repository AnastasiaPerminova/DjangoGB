from django import forms


class ProductFormUpdate(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':
                                                                             'form-control',
                                                                         'placeholder': 'Введите название товара'}),
                           required=False)
    description = forms.CharField(max_length=400, widget=forms.Textarea, required=False)
    price = forms.DecimalField(min_value=0, max_digits=10, decimal_places=2, required=False)
    quantity = forms.IntegerField(min_value=0, required=False)
    image = forms.ImageField(required=False)


