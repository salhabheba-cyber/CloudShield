"""
CloudShield - IAM Policy Manager
"""

import boto3
import json
import os
from dotenv import load_dotenv

load_dotenv()

class IAMPolicyManager:
    def __init__(self):
        self.iam_client = boto3.client(
            'iam',
            aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
            aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'),
            region_name=os.getenv('AWS_DEFAULT_REGION', 'us-east-1')
        )
    
    def create_policy(self, policy_name, policy_document):
        try:
            response = self.iam_client.create_policy(
                PolicyName=policy_name,
                PolicyDocument=json.dumps(policy_document)
            )
            return response['Policy']
        except Exception as e:
            return {"error": str(e)}

POLICY_TEMPLATES = {
    'read_only': {
        "Version": "2012-10-17",
        "Statement": [{
            "Effect": "Allow",
            "Action": ["s3:GetObject", "s3:ListBucket"],
            "Resource": ["arn:aws:s3:::BUCKET_NAME", "arn:aws:s3:::BUCKET_NAME/*"]
        }]
    },
    'write_only': {
        "Version": "2012-10-17",
        "Statement": [{
            "Effect": "Allow",
            "Action": ["s3:PutObject", "s3:DeleteObject"],
            "Resource": "arn:aws:s3:::BUCKET_NAME/*"
        }]
    },
    'full_access': {
        "Version": "2012-10-17",
        "Statement": [{
            "Effect": "Allow",
            "Action": "s3:*",
            "Resource": ["arn:aws:s3:::BUCKET_NAME", "arn:aws:s3:::BUCKET_NAME/*"]
        }]
    }
}
