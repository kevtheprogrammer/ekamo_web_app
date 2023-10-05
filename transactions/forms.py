from django import forms
from .models import FispTransactionManager
from account.models import AgentProfile

class FilterForm(forms.Form):
    agent = forms.ModelChoiceField(
        queryset=AgentProfile.objects.all(),
        empty_label="Select Agent",  # Optional empty label for the dropdown
        widget=forms.Select(attrs={'class': 'form-control'}),
    )
    timestamp = forms.DateField(
        input_formats=['%Y-%m-%d'],  # Define your desired date format here
        widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
    )
    date_to = forms.DateField(
        input_formats=['%Y-%m-%d'],  # Define your desired date format here
        widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
    )

    def __init__(self, user, *args, **kwargs):
        super(FilterForm, self).__init__(*args, **kwargs)
        # Filter the queryset of the agent field based on user.agents_to_manage
        self.fields['agent'].queryset = user.agents_to_manage.all()
