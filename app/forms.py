from django import forms



class contactform(forms.Form):
    name = forms.CharField(max_length=100, required=True, label='Nom')
    email = forms.EmailField(required=True, label='Email')
    message = forms.CharField(widget=forms.Textarea, required=True, label='Message')