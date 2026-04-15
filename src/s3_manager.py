"""
CloudShield - S3 Bucket Manager
"""

import boto3
import json
import os
from dotenv import load_dotenv

load_dotenv()

class S3BucketManager:
    def __init__(self):
        self.session = boto3.Session(
            aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
            aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'),
            region_name=os.getenv('AWS_DEFAULT_REGION', 'us-east-1')
        )
        self.s3_client = self.session.client('s3')
    
    def list_buckets(self):
        try:
            response = self.s3_client.list_buckets()
            return response.get('Buckets', [])
        except Exception as e:
            print(f"Error listing buckets: {e}")
            return []
    
    def create_bucket(self, bucket_name):
        try:
            if self.session.region_name == 'us-east-1':
                response = self.s3_client.create_bucket(Bucket=bucket_name)
            else:
                response = self.s3_client.create_bucket(
                    Bucket=bucket_name,
                    CreateBucketConfiguration={'LocationConstraint': self.session.region_name}
                )
            return response
        except Exception as e:
            print(f"Error creating bucket: {e}")
            return None
    
    def get_bucket_policy(self, bucket_name):
        try:
            response = self.s3_client.get_bucket_policy(Bucket=bucket_name)
            return response.get('Policy', None)
        except Exception as e:
            if 'NoSuchBucketPolicy' in str(e):
                return None
            return None
    
    def set_bucket_policy(self, bucket_name, policy_document):
        try:
            self.s3_client.put_bucket_policy(
                Bucket=bucket_name,
                Policy=json.dumps(policy_document)
            )
            return True
        except Exception as e:
            print(f"Error setting policy: {e}")
            return False
