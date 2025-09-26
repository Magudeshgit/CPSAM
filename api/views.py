import os
import re
import boto3
from botocore.client import Config
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet, ModelViewSet
from rest_framework.decorators import action
from .models import *
from .serializer import *
from core.models import Tags
from rest_framework.permissions import AllowAny

class OperationsViewSet(ViewSet):
    authentication_classes = []
    permission_classes = [AllowAny]
    @action(detail=False, methods=['post'])
    def presigned_url(self, request, *args, **kwargs):
        intent = request.data.get("intent")
        filename = request.data.get("filename")
        print(filename)
        if not filename or type(filename) == str:
            return Response({"success": False, "error": "Filename required as an array"}, status=400)

        ops_mode = "put_object" if intent == "PUT" else "get_object"

        s3_client = boto3.client(
            's3',
            endpoint_url=os.getenv("R2_URL"),
            aws_access_key_id=os.getenv("R2_ACCESS"),
            aws_secret_access_key=os.getenv("R2_SECRET"),
            config=Config(signature_version='v4', region_name='auto')
        )
        url_collection = []
        for i in filename:    
            url = s3_client.generate_presigned_url(
                ops_mode,
                Params={"Bucket": os.getenv("R2_BUCKET"), "Key": i},
                ExpiresIn=3600
            )
            url_collection.append({
                "filename": i,
                "url": url
            })
            

        return Response({"success": True, "url": url_collection})
    @action(detail=False, methods=['post'])
    def add_tag(self, request, *args, **kwargs):
        tag_name = request.data.get('tag_name')
        domain_id = request.data.get('domain_id')
        user = request.data.get('user_id')
        print(tag_name,domain_id,user)
        if not tag_name or not domain_id or not user:
            return Response({"success": False, "error": "tag_name, domain_id, user payload mandatory"}, status=400)
        
        def normalize_string(s: str) -> str:
            return re.sub(r'[^a-z0-9]', '', s.lower())
        
        p, created = Tags.objects.get_or_create(normalized_tag_name=normalize_string(tag_name), defaults={"domain_id":domain_id, "created_by_id":user, "tag_name":tag_name})
        if (not created):
            return Response({"success": True, "message": "Tag Already exists", "Tag_instance": TagSerializer(p).data})
        return Response({"success": True, "message": "Tag Created", "Tag_instance": TagSerializer(p).data}, status=201) 
        
    def list(self, request, *args, **kwargs):
        return Response({"intent":"A general operations endpoint"})
