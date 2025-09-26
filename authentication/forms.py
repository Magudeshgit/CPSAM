from django import forms
from .models import SiteUser, department
class UserUpdateForm(forms.ModelForm):
    username = forms.CharField(disabled=True)
    date_joined = forms.CharField(disabled=True)
    department = forms.CharField(disabled=True)
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.department.dept_name:
            # populate the display field with FK string
            self.fields['department'].initial = str(self.instance.department)
    
    def clean(self):
        cleaned_data = super().clean()
        cleaned_data['department'] = department.objects.get(id=int(cleaned_data.get("department")))
        return cleaned_data
    class Meta:
        model = SiteUser
        fields = ['full_name', 'username', 'email', 'date_joined', 'department', 'yos', 'contact']