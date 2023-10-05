# forms.py
from django import forms
from ..account.models import AgentProfile

class AgentProfileForm(forms.ModelForm):
    class Meta:
        model = AgentProfile
        fields = '__all__'
