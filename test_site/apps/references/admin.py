from django.contrib import admin

from .models import *

admin.site.register([Status,Type,Category,SubCategory])
