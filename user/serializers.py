from django.contrib.auth import authenticate
from django.contrib.auth.models import update_last_login
from rest_framework import serializers
from rest_framework_jwt.settings import api_settings
from userprofile.models import TenderProfile, InputProfile, InvestorProfile, FarmerProfile 
from user.models import User


JWT_PAYLOAD_HANDLER = api_settings.JWT_PAYLOAD_HANDLER
JWT_ENCODE_HANDLER = api_settings.JWT_ENCODE_HANDLER


class FarmerSerializer(serializers.ModelSerializer):
    class Meta:
        model = FarmerProfile
        fields =('first_name', 'last_name', 'phone_number', 'gender')

class TenderSerializer(serializers.ModelSerializer):
    class Meta:
        model = TenderProfile
        fields =('first_name', 'last_name', 'phone_number', 'gender')

class InvestorSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvestorProfile
        fields =('first_name', 'last_name', 'phone_number', 'gender')

class InputSerializer(serializers.ModelSerializer):
    class Meta:
        model = InputProfile
        fields =('first_name', 'last_name', 'phone_number', 'gender')

class FarmerRegistrationSerializer(serializers.ModelSerializer):

    profile = FarmerSerializer(required=False)

    class Meta:
        model = User
        fields = ('email', 'password', 'profile')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        profile_data = validated_data.pop('profile')
        user = User.objects.create_farmeruser(**validated_data)
        FarmerProfile.objects.create(
            user=user,
            first_name = profile_data['first_name'],
            last_name = profile_data['last_name'],
            phone_number = profile_data['phone_number'],
            gender = profile_data['gender']
        )
        return user

class InvestorRegistrationSerializer(serializers.ModelSerializer):

    profile = InvestorSerializer(required=False)
    class Meta:
        model = User
        fields = ('email', 'password', 'profile')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        profile_data = validated_data.pop('profile')
        user = User.objects.create_investoruser(**validated_data)
        InvestorProfile.objects.create(
            user=user,
            first_name = profile_data['first_name'],
            last_name = profile_data['last_name'],
            phone_number = profile_data['phone_number'],
            gender = profile_data['gender']
        )
        return user

class TenderRegistrationSerializer(serializers.ModelSerializer):

    profile = TenderSerializer(required=False)

    class Meta:
        model = User
        fields = ('email', 'password', 'profile')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        profile_data = validated_data.pop('profile')
        user = User.objects.create_tenderuser(**validated_data)
        TenderProfile.objects.create(
            user=user,
            first_name = profile_data['first_name'],
            last_name = profile_data['last_name'],
            phone_number = profile_data['phone_number'],
            gender = profile_data['gender']
        )
        return user

class InputRegistrationSerializer(serializers.ModelSerializer):

    profile = InputSerializer(required=False)

    class Meta:
        model = User
        fields = ('email', 'password', 'profile')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        profile_data = validated_data.pop('profile')
        user = User.objects.create_inputuser(**validated_data)
        InputProfile.objects.create(
            user=user,
            first_name = profile_data['first_name'],
            last_name = profile_data['last_name'],
            phone_number = profile_data['phone_number'],
            gender = profile_data['gender']
        )
        return user

class UserLoginSerializer(serializers.Serializer):

    email = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=128, write_only=True)
    token = serializers.CharField(max_length=255, read_only=True)


    def validate(self, data):
        email = data.get("email", None)
        password = data.get("password", None)
        user = authenticate(email=email, password=password)
        if user is None:
            raise serializers.ValidationError(
                'A user with this email and password is not found'
            )
        try:
            payload = JWT_PAYLOAD_HANDLER(user)
            jwt_token = JWT_ENCODE_HANDLER(payload)
            update_last_login(None, user)
        except User.DoesNotExist:
            raise serializers.ValidationError(
                'User with given email and password does not exist'
            )
        return {
            'email': user.email,
            'token': jwt_token
        }


    


