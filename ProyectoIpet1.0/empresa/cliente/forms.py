from django.contrib.auth import authenticate
from django import forms



class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        password = cleaned_data.get("password")

        if username and password:
            user = authenticate(username=username, password=password)
            if not user or not user.is_active:
                raise forms.ValidationError("Nombre de usuario o contraseña incorrectos.")
        return cleaned_data

