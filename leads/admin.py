from django.contrib import admin

# Register your models here.

from .models import User,Agent,Lead

admin.site.register(User)
admin.site.register(Lead)
admin.site.register(Agent)
