from django import forms

class BookTableForm(forms.Form):
    email = forms.CharField(
        max_length=150,
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your Email'})
    )
    no_of_people = forms.CharField(
        label='Number Of People',
        max_length=150,
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Number Of People'})
    )
    date_and_time = forms.CharField(
        label='Date And Time',
        max_length=150,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Date And Time'})
    )