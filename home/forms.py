from django import forms
from .models import Start

class StartForm(forms.ModelForm):
	class Meta:
		model = Start
		fields = ('style_1_1', 'style_1_2', 'style_1_3', 'style_2', 'style_3', 'style_4', 'style_5', 'style_6', 'size_top', 'size_bottom', 'kakao', 'address',)