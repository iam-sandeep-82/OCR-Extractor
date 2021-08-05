import boto3
import json
import os 

def main(subject, message):
    topic_arn='arn:aws:sns:us-west-2:468141455281:OTP-CONFIRM-SNS'
    sns_client=boto3.client(
        'sns',  
        aws_access_key_id=os.getenv('access_key'),
        aws_secret_access_key=os.getenv('secret_access_key'),
        region_name='ap-south-1',
    )
    response=sns_client.publish(TopicArn=topic_arn,
                                Subject=subject,
                                Message=json.dumps(message),
                                )
