from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from account.models import User
from django.contrib.auth import authenticate

class LoginForm(ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')
        error_messages = {
            'username': {
                'required': 'Введите логин'
            },
            'password': {
                'required': 'Введите пароль'
            }
        }

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError("Ошибка входа")
            return self.cleaned_data

    @property
    def custom_single_error(self):
        default_errors = self.errors
        for field_name, field_errors in default_errors.items():  # TODO
            return field_errors[0]


class RegisterForm(UserCreationForm):
    email = forms.EmailField(
        error_messages={
            'required': 'Введите логин SIGMA',
            'invalid': 'Введите корректный логин SIGMA',
        }
    )
    password1 = forms.CharField(
        error_messages={'required': 'Введите пароль'}
    )
    password2 = forms.CharField(
        error_messages={'required': 'Введите пароль ещё раз'}
    )

    class Meta:
        model = User
        fields = ('email',)

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        if commit:
            user.save()
        return user

    @property
    def custom_single_error(self):
        default_errors = self.errors
        for field_name, field_errors in default_errors.items():  # TODO
            return field_errors[0]