from django.db import models
from PIL import Image
import cv2
import os
from datetime import datetime as dt

from django.utils import timezone

# date formattating
curr_date=dt.now()
curr_time=curr_date.time()

class File(models.Model):

  photo=models.ImageField(blank=False)
  upload_time=models.TimeField(blank=False,default=curr_time)


  def name_normalize(self):
    return str(self.photo.name).replace(' ','_')

  def save(self):
    curr_date=dt.now()
    curr_time=curr_date.time()
    print(f'curr time is {curr_time}')
    self.upload_time=curr_time
    self.photo.name=self.name_normalize()
    super().save()


  def __str__(self):
    return self.photo.name

  class Meta:
    verbose_name = 'Upload File'
    # verbose_name_plural = 'imag'
  
    
  
  