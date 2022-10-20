from django.contrib import admin
from .models import Tender, Input, Investor

# Register your models here.

admin.site.register((Tender, Input, Investor))
