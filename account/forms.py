#encoding: utf-8

from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from .models import User

class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label=_('account.form.user.password1'), widget=forms.PasswordInput)
    password2 = forms.CharField(label=_('account.form.user.password2'), widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'nickname', )

    def clean_password2(self):
        cleaned_data = self.cleaned_data

        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError(_("error.password2"))
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        exclude = ("created_at", "updated_at", "deleted_at", )

    def clean_password(self):
        return self.initial["password"]