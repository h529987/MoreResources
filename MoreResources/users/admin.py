from django.contrib import admin

# Register your models here.
from .models import normal_user, expert, administrator

admin.site.register(normal_user)
admin.site.register(expert)
admin.site.register(administrator)