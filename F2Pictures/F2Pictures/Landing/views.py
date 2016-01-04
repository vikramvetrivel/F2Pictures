# Create your views here.
from django.shortcuts import render
from F2Pictures.Landing.models import Company
from F2Pictures.Landing.serializers import CompanySerializer, UserSerializer
from django.contrib.auth.models import User
from rest_framework import generics

# F2Pictures Master Home Page
def homePage(request):
    """
    Renders the basic layout for the home page
    """
    return render(request, 'HTML/index.html')


class CompanyList(generics.ListCreateAPIView):
    """
    List all Companies, or create a new Company
    """
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class CompanyDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retreive, Update or Delete a particular Company
    """
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
