from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(File)
class FileAdmin(admin.ModelAdmin):
  list_display=['id','photo','upload_time']


# import django.apps

# list_all_models=django.apps.apps.get_models()
# print(list_all_models)
# try:
#   for model in list_all_models:
#     admin.site.register(model)
# except admin.sites.AlreadyRegistered:
#   pass
  

 