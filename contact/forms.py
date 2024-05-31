from django import forms



class ContactForm(forms.Form):
    email = forms.CharField(
        label='Email',
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Your Email'})
    )
    subject = forms.CharField(
        label='Subject',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Subject'})
    )
    message = forms.CharField(
        label='Message',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Message'})
    )