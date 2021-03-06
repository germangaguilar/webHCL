from django import forms
from django.contrib.auth import get_user_model


# Create your forms here.

class ContactForm(forms.Form):
	first_name = forms.CharField(max_length = 50)
	last_name = forms.CharField(max_length = 50)
	email_address = forms.EmailField(max_length = 150)
	message = forms.CharField(widget = forms.Textarea, max_length = 3000)


non_allowed_usernames = ['abc']
# check for unique email & username

User = get_user_model()


class RegisterForm(forms.Form):
    nombre = forms.CharField(label='Nombre')
    apellidos = forms.CharField(label='Apellidos')
    email = forms.EmailField(label='Correo electrónico',
        max_length=254,
        widget=forms.EmailInput(attrs={'style': 'border-color: green;'}),
        help_text='ejemplo@mail.com')
    password1 = forms.CharField(
        label='Contraseña',
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "id": "user-password"
            }
        )
    )
    password2 = forms.CharField(
        label='Confirmar contraseña',
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "id": "user-confirm-password"
            }
        )
    )

    def clean_username(self):
        nombre = self.cleaned_data.get("nombre")
        apellidos = self.cleaned_data.get("apellidos")
        """
        if username in non_allowed_usernames:
            raise forms.ValidationError("This is an invalid username, please pick another.")
        if qs.exists():
            raise forms.ValidationError("This is an invalid username, please pick another.")
            """
        return nombre, apellidos

    def clean_email(self):
        email = self.cleaned_data.get("email")
        qs = User.objects.filter(email__iexact=email)
        if qs.exists():
            raise forms.ValidationError("¡Este correo ya ha sido registrado!")
        return email



class LoginForm(forms.Form):
    email = forms.CharField(widget=forms.TextInput(
        attrs={
        "class": "form-control"
    }))
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "id": "user-password"
            }
        )
    )
    # def clean(self):
    #     data = super().clean()
    #     username = data.get("username")
    #     password = data.get("password")

    def clean_username(self):
        email = self.cleaned_data.get("email")
        qs = User.objects.filter(email__iexact=email) # thisIsMyUsername == thisismyusername
        if not qs.exists():
            raise forms.ValidationError("¡Este correo no está registrado!")
        if qs.count() != 1:
            raise forms.ValidationError("¡Este correo no está registrado!")
        return email
