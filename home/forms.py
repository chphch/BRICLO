from django import forms
from .models import Start

class StartForm(forms.ModelForm):
	class Meta:
		model = Start
		fields = ('curriculum', 'style_1_1', 'style_1_2', 'style_1_3', 'style_2', 'style_3', 'style_4', 'style_5', 'style_6', 'style_7', 'style_8','style_9','style_10','style_11','style_12','height','weight', 'size_top', 'size_bottom', 'kakao', 'address','delivery')