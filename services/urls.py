from rest_framework.routers import DefaultRouter
from django.urls import path, include
from services import views

from . import views

router = DefaultRouter()
router.register(r'tender', views.TenderViewSet,basename="tender")
router.register(r'input', views.InputViewSet,basename="input")
router.register(r'investor', views.InvestorViewSet,basename="investor")


urlpatterns = [
    path('', include(router.urls)),
]

