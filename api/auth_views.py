from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate as auth
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status

from authentication.models import SiteUser, department,  staff_designation
from .serializer import *

class User_Accounts(ModelViewSet):
    queryset = SiteUser.objects.all()
    secondary_queryset = department.objects.all()
    tertiary_queryset = staff_designation.objects.all()
    
    serializer_class = AccountSerializer
    
    
    
    def list(self, request, *args, **kwargs):
        payload = {
            "fields": [i.name for i in SiteUser._meta.get_fields()],
            "department": DepartmentSerializer(self.secondary_queryset, many = True).data,
            "staff_designations": StaffDesignationSerializer(self.tertiary_queryset, many=True).data
            }
        return Response(payload)
    
    def create(self, request, *args, **kwargs):
        request.data['password'] = make_password(request.data['password'])
        print(request.data)
        resp=super().create(request, *args, **kwargs)
        resp.data.pop("password")
        return resp
    
    @action(detail=False, methods=['post'])
    def authenticate(self, request, *args, **kwargs):
        user = auth(None, username=request.data['username'], password=request.data['password'])
        if user is not None:
            resp = AccountSerializer(user).data
            resp.pop("password")
            return Response(resp)
        else:
            return Response({"success": False,"message":"invalid credentials"}, status=status.HTTP_403_FORBIDDEN)
        

    
    