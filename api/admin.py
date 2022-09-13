from django.contrib import admin
from .models import HadishModel
# Register your models here.

@admin.register(HadishModel)
class HadishAdmin(admin.ModelAdmin):
    list_display=['id','hadish_name','narated_by','created_at']
