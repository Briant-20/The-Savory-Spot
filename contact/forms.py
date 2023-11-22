from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=100, label="Name", widget=forms.TextInput(attrs={
            'class': 'form-control', 'placeholder': 'Name'}))
    message = forms.CharField(
        widget=forms.Textarea(attrs={
            'rows': 5, 'class': 'form-control', 'placeholder': 'Message'}))
