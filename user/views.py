from rest_framework import status
from rest_framework.generics import CreateAPIView, RetrieveAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from user.serializers import (FarmerRegistrationSerializer, InvestorRegistrationSerializer,
        TenderRegistrationSerializer, InputRegistrationSerializer)
from user.serializers import UserLoginSerializer
from .models import User

# Create your views here.

class FarmerRegistrationView(CreateAPIView):
    
    serializer_class = FarmerRegistrationSerializer
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        response = {
            'success' : 'True',
            'status code' : status.HTTP_200_OK,
            'message' : 'Farmer registered successfully',
        }
        status_code =  status.HTTP_200_OK
        return Response(response, status_code)

class InvestorRegistrationView(CreateAPIView):
    
    serializer_class = InvestorRegistrationSerializer
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        response = {
            'success' : 'True',
            'status code' : status.HTTP_200_OK,
            'message' : 'Investor registered successfully',
        }
        status_code =  status.HTTP_200_OK
        return Response(response, status_code)


class InputRegistrationView(CreateAPIView):
    
    serializer_class = InputRegistrationSerializer
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        response = {
            'success' : 'True',
            'status code' : status.HTTP_200_OK,
            'message' : 'Input holder registered successfully',
        }
        status_code =  status.HTTP_200_OK
        return Response(response, status_code)

class TenderRegistrationView(CreateAPIView):
    
    serializer_class = TenderRegistrationSerializer
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        response = {
            'success' : 'True',
            'status code' : status.HTTP_200_OK,
            'message' : 'Tender holder registered successfully',
        }
        status_code =  status.HTTP_200_OK
        return Response(response, status_code)

class UserLoginView(APIView):
    permission_classes = (AllowAny,)
    serializer_class = UserLoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        response = {
            'success' : 'True',
            'status code' : status.HTTP_200_OK,
            'message' : 'User logged in successfully',
            'token' : serializer.data['token']
        }
        status_code = status.HTTP_200_OK

        return Response(response, status_code)






