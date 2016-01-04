"""
REST Serializers
"""

from rest_framework import serializers
from F2Pictures.Landing.models import Category, Company, Client, Portfolio, Project
from django.contrib.auth.models import User


class CompanySerializer(serializers.ModelSerializer):

    record_created_by = serializers.ReadOnlyField(source='record_created_by.username')

    class Meta:
        model = Company
        fields = ('id', 'name', 'address_line_1', 'address_line_2', 'state', 'pin', 'phone', 'record_created_by')


class UserSerializer(serializers.ModelSerializer):

    company = serializers.PrimaryKeyRelatedField(many=True, queryset=Company.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'company')


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('id', 'category_name')


class ClientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Client
        fields = ('id', 'first_name', 'last_name', 'company_name', 'phone_number', 'email')


class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = ('id', 'project_name', 'client', 'shoot_date', 'shoot_information')


class PortfolioSerializer(serializers.ModelSerializer):

    class Meta:
        model = Portfolio
        fields = ('id', 'category', 'image_src', 'information', 'project')
