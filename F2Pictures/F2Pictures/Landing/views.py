# Create your views here.
from django.shortcuts import render
from F2Pictures.Landing.models import Company, Portfolio, Project, Client, Category
from F2Pictures.Landing.serializers import CompanySerializer, UserSerializer, PortfolioSerializer
from F2Pictures.Landing.serializers import ProjectSerializer, ClientSerializer, CategorySerializer
from django.contrib.auth.models import User
from rest_framework import permissions, viewsets

# F2Pictures Master Home Page


def homePage(request):
    """
    Renders the basic layout for the home page
    """
    return render(request, 'HTML/index.html')

def packery(request):
    """
    Renders the basic layout for the home page
    """
    return render(request, 'HTML/packery.html')

class CompanyViewSet(viewsets.ModelViewSet):

    """
    List all Companies, or create a new Company
    """
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class PortfolioViewSet(viewsets.ModelViewSet):
    queryset = Portfolio.objects.all()
    serializer_class = PortfolioSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
