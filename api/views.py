from django.shortcuts import render
from .models import HadishModel
from .serializers import HadishSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
# Create your views here.

class HadishAPIView(APIView):
    def get(self,request,pk=None):
        id=pk
        if id is not None:
            hadish=HadishModel.objects.get(id=id)
            serializer=HadishSerializer(hadish)
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            hadishes=HadishModel.objects.all()
            serializer=HadishSerializer(hadishes,many=True)
            return Response(serializer.data,status=status.HTTP_200_OK)

