from django.contrib import admin
from .models import *
from django.contrib.admin import ModelAdmin

from import_export.admin import ImportExportMixin
from import_export.resources import ModelResource

admin.site.register([department, stream, staff_designation])

class UserResource(ModelResource):
    class Meta:
        model = SiteUser
        fields = ['username', 'password', 'email', 'faculty', 'user_type']

class UserModel(ImportExportMixin, admin.ModelAdmin):
    resource_classes = [UserResource]
    list_display = ['username', 'full_name', 'email', 'user_type']
    search_fields = ['username', 'full_name']
    
    # export_form_class = submissioncustomexport
    # list_filter = ['macroevent__eventname', 'microevent', 'registrar__department', 'registrar__yos',]
    
    # def get_export_resource_kwargs(self, request, **kwargs):
    #     exportform = kwargs.get('export_form')
    #     if exportform:
    #         kwargs.update(microevent_id = exportform.cleaned_data["microevent"].id)
    #     return kwargs
    # list_display = ('macroevent','registrar__full_name', 'registrar__username', 'registrar__contact')
        
admin.site.register(SiteUser, UserModel)