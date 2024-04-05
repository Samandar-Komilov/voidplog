from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# We are using default User
# In case of CustomUser we would need to override the ready-to-use UserAuthForms.


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']