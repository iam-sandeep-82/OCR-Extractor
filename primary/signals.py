from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import *
from .file_delete import *

@receiver(post_save, sender=File)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
      # Do what you have to do
      pass
      
        

