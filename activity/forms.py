from django import forms
from .models import *


class CompetitionForm(forms.ModelForm):
    approved_by = forms.BooleanField(widget=forms.HiddenInput(), required=False)
    approval_timestamp = forms.BooleanField(widget=forms.HiddenInput(), required=False)
    from_date = to_date = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={
            'type': 'datetime-local',   # HTML5 datetime picker
            'class': 'form-control',    # optional for styling (Bootstrap/Tailwind etc.)
        }))
    certificate = forms.FileField()
    support_docs = forms.FileField()
    
    class Meta:
        model = Competition
        fields = ['title', 'domain', 'event_level', 'institution','organizer_name','location_link', 'from_date', 'to_date', 'result']
