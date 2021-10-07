import boto3
from botocore.config import Config

class Boto3Client:
    def __init__(self, clientType=''):
        self.clientType = clientType

    def returnClient(self):
        return boto3.client(self.clientType,)

