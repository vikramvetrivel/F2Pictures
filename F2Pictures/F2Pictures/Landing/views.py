# Create your views here.
from django.shortcuts import render

def homePage(request):
    """
    Renders the basic layout for the home page
    """

    return render(request, 'HTML/index.html')