from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control'
            }
        ),
        max_length=45
    )
    password = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'type': 'password'
            }
        ), 
        required=True,
        max_length=45
    )

class PostForm(forms.Form):
    title = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control'
            }
        ),
        max_length=256
    )
    content = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class': 'form-control'
            }
        ), 
        required=True,
        max_length=2048
    )