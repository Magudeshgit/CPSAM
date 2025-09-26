from django import forms
from .models import *

class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True
    is_required = True


class MultipleFileField(forms.FileField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("widget", MultipleFileInput())
        super().__init__(*args, **kwargs)

    def clean(self, data, initial=None):
        single_file_clean = super().clean
        if isinstance(data, (list, tuple)):
            result = [single_file_clean(d, initial) for d in data]
        else:
            result = [single_file_clean(data, initial)]
        return result

class CompetitionForm(forms.ModelForm):
    approved_by = forms.BooleanField(widget=forms.HiddenInput(), required=False)
    approval_timestamp = forms.BooleanField(widget=forms.HiddenInput(), required=False)
    from_date = to_date = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={
            'type': 'datetime-local',   # HTML5 datetime picker
            'class': 'form-control',    # optional for styling (Bootstrap/Tailwind etc.)
        }))
    institution = forms.CharField(label="Organizing Insitution", required=True)
    def clean(self):
        cleaned_data = super().clean()
        from_date = cleaned_data.get("from_date")
        to_date = cleaned_data.get("to_date")

        if from_date and to_date and from_date > to_date:
            self.add_error("from_date", "Number of days cannot be negative")

        return cleaned_data
        
    # support_docs = forms.FileField(widget=forms.HiddenInput(), required=False)
    # event_id = forms.FileField(widget=forms.ClearableFileInput(), required=True)
    # participation_photos = MultipleFileField()
    # brochures = forms.FileField(widget=forms.ClearableFileInput(), required=True)
    # certificate = forms.FileField(widget=forms.ClearableFileInput(), required=True)
    
    
    class Meta:
        model = Competition
        fields = ['title', 'domain', 'event_level', 'institution','organizer_name','location_link', 'from_date', 'to_date', 'result', 'certificate', 'brochures', 'participation_photos', 'event_id']


class CourseForm(forms.ModelForm):
    approved_by = forms.BooleanField(widget=forms.HiddenInput(), required=False)
    approval_timestamp = forms.BooleanField(widget=forms.HiddenInput(), required=False)
    from_date = to_date = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={
            'type': 'datetime-local',   # HTML5 datetime picker
            'class': 'form-control',    # optional for styling (Bootstrap/Tailwind etc.)
        }))
    def clean(self):
        cleaned_data = super().clean()
        from_date = cleaned_data.get("from_date")
        to_date = cleaned_data.get("to_date")

        if from_date and to_date and from_date > to_date:
            self.add_error("from_date", "Number of days cannot be negative")

        return cleaned_data
        
    # support_docs = forms.FileField(widget=forms.HiddenInput(), required=False)
    # event_id = forms.FileField(widget=forms.ClearableFileInput(), required=True)
    # participation_photos = MultipleFileField()
    # brochures = forms.FileField(widget=forms.ClearableFileInput(), required=True)
    # certificate = forms.FileField(widget=forms.ClearableFileInput(), required=True)
    title = forms.CharField(label="Course Title")
    
    class Meta:
        model = Course_Completion
        # fields = ['title', 'domain', 'event_level', 'institution','organizer_name','location_link', 'from_date', 'to_date', 'result', 'certificate', 'brochures', 'participation_photos', 'event_id']
        fields = ['title', 'domain', 'institution', 'course_provider', 'from_date', 'to_date','verification_url', 'certificate']
        

class WorkshopForm(forms.ModelForm):
    approved_by = forms.BooleanField(widget=forms.HiddenInput(), required=False)
    approval_timestamp = forms.BooleanField(widget=forms.HiddenInput(), required=False)
    from_date = to_date = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={
            'type': 'datetime-local',   # HTML5 datetime picker
            'class': 'form-control',    # optional for styling (Bootstrap/Tailwind etc.)
        }))
    def clean(self):
        cleaned_data = super().clean()
        from_date = cleaned_data.get("from_date")
        to_date = cleaned_data.get("to_date")

        if from_date and to_date and from_date > to_date:
            self.add_error("from_date", "Number of days cannot be negative")

        return cleaned_data
        
    # support_docs = forms.FileField(widget=forms.HiddenInput(), required=False)
    # event_id = forms.FileField(widget=forms.ClearableFileInput(), required=True)
    # participation_photos = MultipleFileField()
    # brochures = forms.FileField(widget=forms.ClearableFileInput(), required=True)
    # certificate = forms.FileField(widget=forms.ClearableFileInput(), required=True)
    # title = forms.CharField(label="Course Title")
    
    class Meta:
        model = Workshop
        fields = ['title', 'domain', 'event_level', 'institution','organizer_name','location_link', 'from_date', 'to_date', 'certificate', 'brochures', 'participation_photos', 'event_id']
        

class PPOForm(forms.ModelForm):
    approved_by = forms.BooleanField(widget=forms.HiddenInput(), required=False)
    approval_timestamp = forms.BooleanField(widget=forms.HiddenInput(), required=False)
    from_date = to_date = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={
            'type': 'datetime-local',   # HTML5 datetime picker
            'class': 'form-control',    # optional for styling (Bootstrap/Tailwind etc.)
        }))
    def clean(self):
        cleaned_data = super().clean()
        from_date = cleaned_data.get("from_date")
        to_date = cleaned_data.get("to_date")

        if from_date and to_date and from_date > to_date:
            self.add_error("from_date", "Number of days cannot be negative")

        return cleaned_data
        
    # support_docs = forms.FileField(widget=forms.HiddenInput(), required=False)
    # event_id = forms.FileField(widget=forms.ClearableFileInput(), required=True)
    # participation_photos = MultipleFileField()
    # brochures = forms.FileField(widget=forms.ClearableFileInput(), required=True)
    # certificate = forms.FileField(widget=forms.ClearableFileInput(), required=True)
    # title = forms.CharField(label="Course Title")
    
    class Meta:
        model = Preplacement
        fields = ['domain', 'organization', 'ppo_type', 'role', 'from_date', 'to_date', 'location_link', 'github_link', 'certificate']
        # fields = '__all__'

class ProjectForm(forms.ModelForm):
    approved_by = forms.BooleanField(widget=forms.HiddenInput(), required=False)
    approval_timestamp = forms.BooleanField(widget=forms.HiddenInput(), required=False)
    from_date = to_date = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={
            'type': 'datetime-local',   # HTML5 datetime picker
            'class': 'form-control',    # optional for styling (Bootstrap/Tailwind etc.)
        }))
    def clean(self):
        cleaned_data = super().clean()
        from_date = cleaned_data.get("from_date")
        to_date = cleaned_data.get("to_date")

        if from_date and to_date and from_date > to_date:
            self.add_error("from_date", "Number of days cannot be negative")

        return cleaned_data
        
    # support_docs = forms.FileField(widget=forms.HiddenInput(), required=False)
    # event_id = forms.FileField(widget=forms.ClearableFileInput(), required=True)
    # participation_photos = MultipleFileField()
    # brochures = forms.FileField(widget=forms.ClearableFileInput(), required=True)
    # certificate = forms.FileField(widget=forms.ClearableFileInput(), required=True)
    title = forms.CharField(label="Project Title")
    problem_statement = forms.CharField(widget=forms.Textarea(attrs={"class": "cols-span-full"}))
    
    class Meta:
        model = Project
        fields = ['title', 'domain', 'project_type','from_date', 'to_date', 'github_link', 'problem_statement', 'prototype_video']
        # fields = '__all__'