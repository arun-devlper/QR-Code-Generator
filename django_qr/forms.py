from django import forms

class QRCodeForm(forms.Form):
    content_name = forms.CharField(
        max_length=50, 
        label='Content name',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter Content Name'
        })
        )
    url = forms.URLField(
        max_length=200,
        label='Content URL',
        widget=forms.URLInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter the URL of your online content'
        })
        )