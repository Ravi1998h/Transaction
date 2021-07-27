from django.contrib import admin
from .models import user
@admin.register(user)
class useradmin(admin.ModelAdmin):
    list_display=['name','phone_no','amount_add']

# Register your models here.
