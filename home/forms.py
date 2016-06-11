from django import forms
from .models import Start

class StartForm(forms.ModelForm):
	class Meta:
		model = Start
		fields = ('style1', 'style2', 'style3', 'style4', 'size_top', 'size_bottom', 'kakao', 'address',)