from django import forms

class CommentForm(forms.Form):
    comment = forms.CharField(
        label='Comment',
        max_length=150,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Comment'})
    )
    profession = forms.CharField(
        label='Profession',
        max_length=150,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Profession'})
    )