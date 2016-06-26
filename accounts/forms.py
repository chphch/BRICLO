import re
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, SetPasswordForm, PasswordChangeForm
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.utils.translation import ugettext_lazy as _
from .models import Profile
from django.core import validators
GENDER_CHOICES = (
            ('MEN' , 'MEN'),
            ('WOMEN' , 'WOMEN'),
        )

def phone_validator(value):
    number = ''.join(re.findall(r'\d+', value))
    return RegexValidator(r'^01[016789]\d{7,8}$', message='번호를 입력해주세요')(number)

def isValidUsername(field_data):
    try:
        User.objects.get(username=field_data)
    except User.DoesNotExist:
        return
    raise validators.ValidationError('"%s"는 이미 사용중인 아이디입니다. 다른 아이디를 입력해주세요.' % field_data)

class SignupForm2(UserCreationForm):
	email = forms.EmailField()

	def save(self, commit=True):
		user = super(SignupForm2, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user

class SignupForm(UserCreationForm):
    username = forms.CharField(label='아이디', validators=[isValidUsername])
    password1 = forms.CharField(label='비밀번호', widget=forms.PasswordInput)
    password2 = forms.CharField(label='비밀번호 확인', widget=forms.PasswordInput)
    name = forms.CharField(label='이름')
    email = forms.EmailField(label='이메일')   
    phone = forms.CharField(label='휴대폰 번호', widget=forms.TextInput(attrs={'placeholder': 'ex) 010-1234-5678'}), validators=[phone_validator])
    gender= forms.ChoiceField(label='성별', choices = GENDER_CHOICES)
    is_agree = forms.BooleanField(label='', error_messages={
        'required' : '약관동의를 해주셔야 가입이 됩니다.',
    })
    error_messages = {
        'password_mismatch': _("비밀번호가 일치하지 않습니다."),
    }
    
    def save(self, commit=True):
        user = super(SignupForm, self).save(commit=False)
        if commit:
            user.save()
            user.profile.name = self.cleaned_data['name']
            user.profile.gender = self.cleaned_data['gender']
            user.profile.email = self.cleaned_data['email']
            user.profile.phone = self.cleaned_data['phone']
            user.profile.save()
        return user

class LoginForm(AuthenticationForm):
    username = forms.CharField(label='아이디')
    password = forms.CharField(label='비밀번호', widget=forms.PasswordInput())

class UpdateForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ('email','name','gender', 'phone',)

class PassChangeForm(PasswordChangeForm):
    old_password = forms.CharField(label=_("기존 비밀번호"), widget=forms.PasswordInput(attrs={'autofocus': ''}), )
    new_password1 = forms.CharField(label=_("새 비밀번호"), widget=forms.PasswordInput(),)
    new_password2 = forms.CharField(label=_("새 비밀번호 확인"), widget=forms.PasswordInput(), )
    error_messages = dict(SetPasswordForm.error_messages, **{
        'password_incorrect': _("기존 비밀번호가 일치하지 않습니다. 다시 입력해주세요."),
    })
