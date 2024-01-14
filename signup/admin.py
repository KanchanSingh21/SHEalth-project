from django.contrib import admin

# Register your models here.
from signup.models import signup_details

class signup(admin.ModelAdmin):
    list_display=["email","DOB","address","desination","password","confirm_password"]



admin.site.register(signup_details,signup)