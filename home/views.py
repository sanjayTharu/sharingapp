from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import FileListSerializer

# Create your views here.

def home(request):
    return render(request,'home/index.html')

class HandleFileUpload(APIView):

    def post(self,request):
        try:
            data=request.data

            serializer=FileListSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    'status':200,
                    'message': 'files uploaded successfully'
                })
            return Response({
                'status':400,
                'message':'Bad Request',
                'data': serializer.errors
            })
        except Exception as e:
            print(e)

