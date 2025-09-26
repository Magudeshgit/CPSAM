from rest_framework import serializers
from authentication.models import *
from core.models import Tags

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = SiteUser
        fields = '__all__'
        
class DepartmentSerializer(serializers.ModelSerializer):
    dept_name = serializers.CharField()
    class Meta:
        model = department
        fields = '__all__'

class StaffDesignationSerializer(serializers.ModelSerializer):
    class Meta:
        model = staff_designation
        fields = '__all__'
    
class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tags
        fields = '__all__'