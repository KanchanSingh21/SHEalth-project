from django.contrib import admin

# Register your models here.
from login.models import login_details

class login(admin.ModelAdmin):
    list_display=["email","password"]



admin.site.register(login_details,login)