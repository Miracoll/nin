from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from nin_record.api.serializers import GuardianSerializer, NINProfileSerializer, NextOfKinSerializer, ParentSerializer, SupportingDocumentSerializer
from nin_record.models import NINProfile, NextOfKin, Parent, SupportingDocument, Guardian

class NINReportList(APIView):
    def get(self, request):
        data = NINProfile.objects.all()
        serializer = NINProfileSerializer(data, many=True)
        return Response(serializer.data)

    def post(self, request):
        # email = request.data.get('email')
        # if NINProfile.objects.filter(email=email).exists():
        #     return Response(
        #         {"error": "Email already exists."},
        #         status=status.HTTP_400_BAD_REQUEST
        #     )
        
        serializer = NINProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class NINReportDetail(APIView):
    def get(self, request, pk):
        try:
            data = NINProfile.objects.get(pk=pk)
        except NINProfile.DoesNotExist:
            return Response({'error':'Record not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = NINProfileSerializer(data)
        return Response(serializer.data)
    
    def put(self, request, pk):
        data = NINProfile.objects.get(pk=pk)
        serializer = NINProfileSerializer(data, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
class SupportingDocumentList(APIView):
    def get(self,request):
        data = SupportingDocument.objects.all()
        serializer = SupportingDocumentSerializer(data, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = SupportingDocumentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class SupportingDocumentDetail(APIView):
    def get(self, request, pk):
        try:
            data = SupportingDocument.objects.get(pk=pk)
        except SupportingDocument.DoesNotExist:
            return Response({'error':'Record not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = SupportingDocumentSerializer(data)
        return Response(serializer.data)
    
    def put(self, request, pk):
        data = SupportingDocument.objects.get(pk=pk)
        serializer = SupportingDocumentSerializer(data, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
class ParentList(APIView):
    def get(self,request):
        data = Parent.objects.all()
        serializer = ParentSerializer(data, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = ParentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class ParentDetail(APIView):
    def get(self, request, pk):
        try:
            data = Parent.objects.get(pk=pk)
        except Parent.DoesNotExist:
            return Response({'error':'Record not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = ParentSerializer(data)
        return Response(serializer.data)
    
    def put(self, request, pk):
        data = Parent.objects.get(pk=pk)
        serializer = ParentSerializer(data, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
class GuardianList(APIView):
    def get(self,request):
        data = Guardian.objects.all()
        serializer = GuardianSerializer(data, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = GuardianSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class GuardianDetail(APIView):
    def get(self, request, pk):
        try:
            data = Guardian.objects.get(pk=pk)
        except Guardian.DoesNotExist:
            return Response({'error':'Record not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = GuardianSerializer(data)
        return Response(serializer.data)
    
    def put(self, request, pk):
        data = Guardian.objects.get(pk=pk)
        serializer = GuardianSerializer(data, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
class NextOfKinList(APIView):
    def get(self,request):
        data = NextOfKin.objects.all()
        serializer = NextOfKinSerializer(data, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = NextOfKinSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class NextOfKinDetail(APIView):
    def get(self, request, pk):
        try:
            data = NextOfKin.objects.get(pk=pk)
        except NextOfKin.DoesNotExist:
            return Response({'error':'Record not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = NextOfKinSerializer(data)
        return Response(serializer.data)
    
    def put(self, request, pk):
        data = NextOfKin.objects.get(pk=pk)
        serializer = NextOfKinSerializer(data, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)