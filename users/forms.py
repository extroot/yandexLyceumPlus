from django import forms

from .models import CustomUser, Profile


class BaseForm(forms.BaseForm):
    """
    BaseForm class based in forms.BaseForm
    In __init__ adds 'form-control' class to all fields
    Честно, я не знаю, как сделать проще сразу для всех полей.
    Прописывать виджеты для каждого поля - это же будет частично считаться хардкодом)
     Да и не удобно это.
    Если есть способ проще, я был бы рад
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'


class UserLoginForm(forms.Form, BaseForm):
    email = forms.EmailField(label='Почта')
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)


class UserRegistrationForm(forms.ModelForm, BaseForm):
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Пароли не совпадают')
        return cd['password2']


class UserForm(forms.ModelForm, BaseForm):
    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'email')


class ProfileForm(forms.ModelForm, BaseForm):
    class Meta:
        model = Profile
        fields = ('birthday', )
        widgets = {
            'birthday': forms.DateInput(attrs={'type': 'date'})
        }
