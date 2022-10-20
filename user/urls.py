from django.urls import path, include
from .views import FarmerRegistrationView, InputRegistrationView, InvestorRegistrationView, TenderRegistrationView, UserLoginView


urlpatterns = [
    path('signup/farmer/', FarmerRegistrationView.as_view(),name='signup_farmer'),
	path('signup/investor/', InvestorRegistrationView.as_view(),name='signup_investor'),
    path('signup/input/', InputRegistrationView.as_view(),name='signup_input'),
	path('signup/tender/', TenderRegistrationView.as_view(),name='signup_tender'),
    path('signin/',UserLoginView.as_view()),
]
