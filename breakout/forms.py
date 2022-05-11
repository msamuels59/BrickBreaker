from django import forms
from .models import Score

# class ScoreForm(forms.ModelForm):
#     class Meta:
#         model = Score
#         fields = ('points', 'player')
#         help_texts = {
#             'player': "Enter your intials"
#         }

class ScoreForm(forms.Form):
    initials = forms.CharField(max_length=5)