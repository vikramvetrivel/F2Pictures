"""Admin Properties for added models"""

from django.contrib import admin
from F2Pictures.Landing.models import *

admin.site.register(Company)
admin.site.register(Portfolio)
admin.site.register(Project)
admin.site.register(Client)
admin.site.register(Category)
