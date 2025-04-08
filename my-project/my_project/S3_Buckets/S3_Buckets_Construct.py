import os
from aws_cdk import (
    aws_s3 as s3
)
from constructs import Construct

class S3BucketsConstruct(Construct):

    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # Creating an S3 bucket
        self.app_data_bucket = s3.Bucket(
            self, 
            id="AppData", 
            bucket_name="maddy-sommer-app-data"
        )