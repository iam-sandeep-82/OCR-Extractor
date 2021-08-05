from . models import *
from datetime import datetime, timedelta
import os
import boto3

def fileDelete():
    array_file=[]
    all_files=File.objects.values()

    for file in all_files:
      delta_1=file['upload_time']
      get_upload_hour=delta_1.hour
      curr_date=datetime.now()
      get_current_hour=curr_date.time().hour
      
      remain_hour=get_current_hour - get_upload_hour

      if remain_hour > 1:

        get_file_id=file['id']
        instance=File.objects.get(id=get_file_id)
        rel_path='https://user-upload-image-container.s3.ap-south-1.amazonaws.com'
        file_name=instance.photo.name
        file_delete_path=os.path.join(rel_path, file_name)
        client=boto3.client(
          's3',  
          aws_access_key_id=os.getenv('access_key'),
          aws_secret_access_key=os.getenv('secret_access_key'),
          region_name='ap-south-1',
          )
        response = client.delete_objects(
            Bucket='user-upload-image-container',
            Delete={
                'Objects': [
                    {
                        'Key': file_name,
                    },
                ],
                'Quiet': False
            },
        )
        dict_file_delete={}
        dict_file_delete['name']=instance.photo.name
        dict_file_delete['upload_at']=get_upload_hour

        array_file.append(dict_file_delete)
        instance.delete()
    
      else:
        print('No File having more than 1 uploaded hour')
    return array_file

