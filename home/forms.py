from django import forms
from .models import Start

class StartForm(forms.ModelForm):
	class Meta:
		model = Start
		fields = ('size_top', 'size_bottom', 'kakao', 'address',)