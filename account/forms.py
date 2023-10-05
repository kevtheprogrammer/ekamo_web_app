from .models import * 

class AgentProfileForm(forms.ModelForm):
    class Meta:
        model = AgentProfile
        fields = [
            'first_name',
            'last_name',
            'floatLimit',
            'code',
            'phonenumber',
            'agent_type',
            'idtype',
            'idNo',
            'id_front',
            'id_back',
            'dob',
            'province',
            'district',
            'account_type',
        ]
