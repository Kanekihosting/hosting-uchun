from django import forms
from django.contrib.auth.models import User



class LoginForm(forms.Form):
    username = forms.CharField(label='username')
    password = forms.CharField(widget=forms.PasswordInput)


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Parol', widget=forms.PasswordInput)

    password_2 = forms.CharField(label='parolni qayta yozing', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

    def clean_password_2(self):
        data = self.cleaned_data
        if data['password'] != data['password_2']:
            raise forms.ValidationError("Ikkala parol bir biriga teng bo'lishi kerak!")
        return data['password_2']


