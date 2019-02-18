from django import forms

from account.models import Account


class AccountForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = Account
