from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import UserChangeForm, UserModel, User

class BlogsForms(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    email = forms.EmailField()

class UserCreationFormCustom(UserCreationForm):
    username = forms.CharField(label="Usuario:")
    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña:", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir contraseña:", widget=forms.PasswordInput)
    class Meta:
        model = UserModel
        fields = ["username", "email", "password1", "password2"]
        #Saca los mensajes de ayuda
        help_texts = {k:"" for k in fields}

class UserEditForm(UserChangeForm):
    password = None
    email = forms.EmailField(label="Ingrese su email: ")
    last_name = forms.CharField(label="Apellido")
    first_name = forms.CharField(label="Nombre")
    imagen = forms.ImageField(label="Avatar", required=False)    
    class Meta:
        model = User
        fields = ["first_name", "last_name", "email", "imagen"]