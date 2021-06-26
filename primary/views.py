# UTITLY MODULE
from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime as dt
from PIL import Image
import os
from django.http import HttpResponse, HttpRequest, JsonResponse
import datetime as dt

# # App to App Modules
from .forms  import *
from .models import *

def index(request):
  context={'obj':'Hello Dynamo'}
  return render(request, './primary/index.html', context=context)


