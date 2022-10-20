from rest_framework import status
from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from user.serializers import FarmerRegistrationSerializer, TenderRegistrationSerializer, InputRegistrationSerializer, InvestorRegistrationSerializer
from userprofile.models import FarmerProfile, InvestorProfile, InputProfile, TenderProfile
from user.models import User

# Create your views here.
class UserProfileView(RetrieveAPIView):

    permission_classes = (IsAuthenticated,)
    authentication_class = ''

    def get(self, request):
        try:
            if request.user.is_farmer == True:
                user_profile = FarmerProfile.objects.get(user=request.user)
                status_code = status.HTTP_200_OK
                response = {
                    'success': 'True',
                    'status code': status_code,
                    'message': 'Farmer profile fetched successfully',
                    'data': [{
                        'first_name': user_profile.first_name,
                        'last_name': user_profile.last_name,
                        'phone_number': user_profile.phone_number,
                        'gender': user_profile.gender,
                    }]
                }

            if request.user.is_investor == True:
                user_profile = InvestorProfile.objects.get(user=request.user)
                status_code = status.HTTP_200_OK
                response = {
                    'success': 'True',
                    'status code': status_code,
                    'message': 'Investor profile fetched successfully',
                    'data': [{
                        'first_name': user_profile.first_name,
                        'last_name': user_profile.last_name,
                        'phone_number': user_profile.phone_number,
                        'gender': user_profile.gender,
                    }]
                }

            if request.user.is_input_holder == True:
                user_profile = InputProfile.objects.get(user=request.user)
                status_code = status.HTTP_200_OK
                response = {
                    'success': 'True',
                    'status code': status_code,
                    'message': 'Input holder profile fetched successfully',
                    'data': [{
                        'first_name': user_profile.first_name,
                        'last_name': user_profile.last_name,
                        'phone_number': user_profile.phone_number,
                        'gender': user_profile.gender,
                    }]
                }

            if request.user.is_tender_holder == True:
                user_profile = TenderProfile.objects.get(user=request.user)
                status_code = status.HTTP_200_OK
                response = {
                    'success': 'True',
                    'status code': status_code,
                    'message': 'Tender holder profile fetched successfully',
                    'data': [{
                        'first_name': user_profile.first_name,
                        'last_name': user_profile.last_name,
                        'phone_number': user_profile.phone_number,
                        'gender': user_profile.gender,
                    }]
                }

            if request.user.is_superuser == True:
                user_profile = User.objects.get(user=request.user)
                status_code = status.HTTP_200_OK
                response = {
                    'success': 'True',
                    'status code': status_code,
                    'message': 'Farmer profile fetched successfully',
                    'data': [{
                        'email' : user_profile.email
                    }]
                }

        except Exception as e:
            status_code = status.HTTP_400_BAD_REQUEST
            response = {
                'success': 'false',
                'status code': status.HTTP_400_BAD_REQUEST,
                'message': 'User does not exist',
                'error': str(e)
            }
        return Response(response, status=status_code)
