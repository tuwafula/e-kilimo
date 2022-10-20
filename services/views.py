from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework import viewsets, status
from django.http import Http404, JsonResponse
from rest_framework.views import Response
from .models import Tender, Input , Investor
from .serializers import TenderViewSerializer, InputViewSerializer, InvestViewSerializer
from rest_framework.decorators import action

# Create your views here.

class TenderViewSet(viewsets.ModelViewSet):
    serializer_class = TenderViewSerializer

    #@action(detail=False, url_path="tender/")
    def get_queryset(self):
        queryset = Tender.objects.all()
        return  queryset

    # #@action(detail=True, methods=['get'])
    # def retrieve(self, request, *args, **kwargs):
    #     params = kwargs
    #     params_list = params['pk'].split('-')
    #     tenders = Tender.objects.filter(
    #         name=params_list[0]
    #     )
    #     serializer = TenderViewSerializer(tenders, many=True)
    #     return Response(serializer.data)
    
    #@action(detail=False, methods=['post'], url_path='add/')
    def create(self, request, *args, **kwargs):

        new_tender = Tender.objects.create(
            name=request.data["name"],
            description=request.data["description"],
            date_due=request.data["date_due"],
            location=request.data["location"],
            contact=request.data['contact']
        )
           
        new_tender.save()
        
        serializer = TenderViewSerializer(new_tender)

        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        try:
            instance =self.get_object()
            self.perform_destroy(instance)
        except Http404:
            pass

        return Response({"message": "Tender deleted successfully"})

    # def update(self, request, *args, **kwargs):
    #     tender_object = self.get_object()
    #     data = request.data
    #     # if not tender_object:
    #     #     return Response({"error"  : "Tender does not exist"})

    #     tender_object.name = data['name']
    #     tender_object.description = data["description"],
    #     tender_object.location = data["location"],
    #     tender_object.contact = data['contact']

    #     tender_object.save()

    #     serializer = TenderViewSerializer(tender_object)

    #     return Response(serializer.data)




class InvestorViewSet(ModelViewSet):
    serializer_class = InvestViewSerializer
    queryset = Investor.objects.all()

    def get_queryset(self):
        queryset = Investor.objects.all()
        return  queryset

    def create(self, request, *args, **kwargs):

        new_investment = Investor.objects.create(
            name=request.data["name"],
            description=request.data["description"],
            location=request.data["location"],
            contact=request.data['contact']
        )
           
        new_investment.save()
        
        serializer = InvestViewSerializer(new_investment)

        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        try:
            instance =self.get_object()
            self.perform_destroy(instance)
        except Http404:
            pass

        return Response({"message": "Investment deleted successfully"})



class InputViewSet(ModelViewSet):
    serializer_class = InputViewSerializer
    queryset = Input.objects.all()

    def get_queryset(self):
        queryset = Input.objects.all()
        return  queryset

    def create(self, request, *args, **kwargs):

        new_input = Input.objects.create(
            name=request.data["name"],
            description=request.data["description"],
            price=request.data["price"],
            quantity=request.data["quantity"],
            contact=request.data['contact']
        )
           
        new_input.save()
        
        serializer = InputViewSerializer(new_input)

        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        try:
            instance =self.get_object()
            self.perform_destroy(instance)
        except Http404:
            pass

        return Response({"message": "Input deleted successfully"})



