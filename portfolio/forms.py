from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=30)
    subject = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)
