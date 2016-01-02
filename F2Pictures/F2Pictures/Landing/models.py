from django.db import models
from django.core.validators import URLValidator
from django.core.validators import EmailValidator

# Create your models here.


class Company(models.Model):
    name = models.CharField(unique=True, max_length = 50)

class Client(models.Model):
    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length = 30)
    company_name = models.ForeignKey(Company)
    phone_number = models.PositiveIntegerField()
    email = models.EmailField()
    
class Project(models.Model):
    project_name = models.CharField(primary_key=True, max_length = 50)
    client_id = models.ForeignKey(Client)
    shoot_date = models.DateField()
    shoot_information = models.TextField()

class Category(models.Model):
    category_name = models.CharField(max_length = 50, unique=True)

class Portfolio(models.Model):
    image_id = models.AutoField(primary_key=True)
    category = models.ForeignKey(Category)
    image_src = models.TextField(validators=[URLValidator()], unique=True)
    information = models.TextField()
    project = models.ForeignKey(Project)

