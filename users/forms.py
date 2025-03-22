from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User


class UserCreateForm(forms.ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput, required=True)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password', 'confirm_password']
        widgets = {
            'password': forms.PasswordInput(),
            'confirm_password': forms.PasswordInput(),
        }


    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        if password != confirm_password:
            raise forms.ValidationError('Parolni to\'g\'ri kiriting!')
        return cleaned_data

    def clean_password(self):
        password = self.cleaned_data['password']
        if not any(char.isdigit() for char in password):
            raise forms.ValidationError('Parolda kamida 1 ta son bo\'lishi kerak!')
        if not any(char.isalpha() for char in password):
            raise forms.ValidationError('Parolda kamida 1 ta harf bo\'lishi kerak!')
        if not any(char.islower() for char in password):
            raise forms.ValidationError('Parolda kamida 1 ta kichkina harf bo\'lishi kerak!')
        if not any(char.isupper() for char in password):
            raise forms.ValidationError('Parolda kamida 1 ta katta harf bo\'lishi kerak!')
        if len(password) < 8 or (len(password) > 20):
            raise forms.ValidationError('Parol 8 tadan 20 tagacha simvol bo\'lishi kerak!')
        return password


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))


    def clean_username(self):
        username = self.cleaned_data['username']
        if not User.objects.filter(username=username).exists():
            raise forms.ValidationError('Bunday foydalanuvchi nomi mavjud emas!')
        return username

class ProfileUpdateForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user





