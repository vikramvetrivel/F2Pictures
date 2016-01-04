"""
REST Serializers
"""

from rest_framework import serializers
from F2Pictures.Landing.models import Category, Company, Client, Portfolio, Project
from django.contrib.auth.models import User

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ('id', 'name', 'address_line_1', 'address_line_2', 'state', 'pin', 'phone')

class UserSerializer(serializers.ModelSerializer):
    company = serializers.PrimaryKeyRelatedField(many=True, queryset=Company.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'company')
