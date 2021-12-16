from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from authapp.models import ShopUser


class ShopUserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class AgeValidatorMixin:
    def clean_age(self):
        age = self.cleaned_data.get('age')
        if age and age < 18:
            raise forms.ValidationError("You're too young!")
        return age


class ShopUserRegisterForm(AgeValidatorMixin, UserCreationForm):
    class Meta:
        model = ShopUser
        fields = ('username', 'password1', 'password2', 'first_name', 'email', 'age')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = f'form-control {field_name}'
            field.help_text = ''


class ShopUserEditForm(AgeValidatorMixin, UserChangeForm):
    class Meta:
        model = ShopUser
        fields = ('username', 'password', 'email', 'first_name', 'last_name', 'age', 'avatar')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = f'form-control {field_name}'
            field.help_text = ''
            if field_name == 'password':
                field.widget = forms.HiddenInput()
