from django.db import models
from django.core.validators import URLValidator
from django.core.validators import EmailValidator
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.


class Company(models.Model):
    name = models.CharField(unique=True, max_length = 50)
    address_line_1 = models.CharField(max_length = 50, blank=True, null=True)
    address_line_2 = models.CharField(max_length = 50, blank=True, null=True)
    state = models.CharField(max_length=3, blank=True, null=True)
    pin = models.PositiveIntegerField(blank=True, null=True)
    phone = PhoneNumberField(blank=True, null=True)

    def __unicode__(self):
        return self.name

class Client(models.Model):
    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length = 30)
    company_name = models.ForeignKey(Company)
    phone_number = PhoneNumberField()
    email = models.EmailField()
    
class Project(models.Model):
    project_name = models.CharField(primary_key=True, max_length = 50)
    client_id = models.ForeignKey(Client)
    shoot_date = models.DateField(blank=True, null=True)
    shoot_information = models.TextField(blank=True, null=True)

class Category(models.Model):
    category_name = models.CharField(max_length = 50, unique=True)

class Portfolio(models.Model):
    image_id = models.AutoField(primary_key=True)
    category = models.ForeignKey(Category)
    image_src = models.TextField(validators=[URLValidator()], unique=True)
    information = models.TextField(blank=True, null=True)
    project = models.ForeignKey(Project, blank=True, null=True)