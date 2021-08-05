# UTITLY MODULE
from django.shortcuts import render,  redirect
from django.http import HttpResponse, Http404
from datetime import datetime as dt
from PIL import Image
import os
from django.http import HttpResponse, HttpRequest, JsonResponse,HttpResponseRedirect
import datetime as dt
from pathlib import Path
from django.contrib import messages
from django.urls import reverse, reverse_lazy, resolve
import boto3

# # App to App Modules
from .forms  import *
from .models import *
from .ocr import *
from .file_delete import *
from .utility import *
from fetcher.storages import MediaStorage

#  ocr modules
import pytesseract as tess
import cv2
import time
import re
tess.pytesseract.tesseract_cmd=r'C:\tesseract\tesseract.exe'


# ------------- INDEX VIEWS ---------------

def index(request):

  if request.method=='POST':
    form=FileForm(request.POST, request.FILES)

    if form.is_valid():
      print(form.cleaned_data)
      file_obj=form.cleaned_data['photo']
      s=form.save()

      # normalize name
      file_name=str(file_obj.name).replace(' ','_')

      # ----------------
      client=boto3.client(
        'textract',  
        aws_access_key_id=os.getenv('access_key'),
        aws_secret_access_key=os.getenv('secret_access_key'),
        region_name='ap-south-1',
        )

      # explicit wait until the uploaded image is save into s3 bucket
      time.sleep(3)

      try:

        # SHUTDOWN FOR TEMP
        response = client.detect_document_text(
          Document={
            "S3Object": { 
            "Bucket": 'user-upload-image-container',
            "Name": file_name,
            }
          }
        )

        raw_string=''
        for i in response['Blocks']:
          if i['BlockType']=='LINE':
            raw_string+=i['Text']

        context={'data': raw_string, 'download_url':'download_url'} 
        messages.success(request, 'Completed, Check your Results!!!')   
        return render(request, './primary/response.html', context)

      except:
        messages.error(request, 'Please Re-Upload the Image Again!')
        return redirect(reverse('INDEX'))


        # METHOD-2 ACCESS ONLY IN LOCAL SYSTEM
        # output=tess.image_to_string(local_path)

        # METHOD-3 SOURCE >>> API
        # media_storage = MediaStorage()
        # request.session['output_string']=str(raw_string)
        
        # ocr_data=ocr(image_path=img_path)
        # raw_string=ocr_data[0]

        # if (raw_string != 'No recognized text !'):
        #   print(raw_string)
        #   process_pages=ocr_data[1]
        #   download_url=ocr_data[2]
        #   error=ocr_data[3]

        #   print(f'process_pages >> {process_pages}')
        #   print(f'Error >> {error}')

        #   context={'data': raw_string, 'process_pages': process_pages,
        #   'download_url':download_url, 'error':error }

    else:
      print('NOT VALIDATED')

  else:
    form=FileForm()

  context={'form':form}
  return render(request, 'primary/index.html', context)



# ------------- RESPONSE VIEWS ---------------
def send_sms_result(request):
  message=request.session.get('raw_string')
  main(subject='Result from web-app fetcher', message=message)


def DeleteFile(request):
    ret_value= fileDelete()
    context={'files':ret_value}
    return render(request, './primary/file_delete.html')



