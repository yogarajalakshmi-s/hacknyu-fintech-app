from django import forms

class PaymentForm(forms.Form):
    amount = forms.DecimalField(max_digits=10, decimal_places=2, min_value=0.01, label='Amount to Pay')
    card_number = forms.CharField(max_length=16, min_length=16, widget=forms.TextInput(attrs={'type': 'number'}), label="Card Number")
    card_expiry = forms.CharField(max_length=5, widget=forms.TextInput(attrs={'placeholder': 'MM/YY'}), label="Expiry Date (MM/YY)")
    card_cvc = forms.CharField(max_length=3, widget=forms.TextInput(attrs={'type': 'number'}), label="CVC")
