from django import forms


class UserForm(forms.Form):
    username = forms.CharField(max_length=65, label='', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Имя пользователя'}))
    password = forms.CharField(max_length=65, label='',
                               widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Пароль'}))