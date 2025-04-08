from aws_cdk import (
    # Duration,
    Stack,
    aws_s3 as s3
)
from constructs import Construct
from my_project.S3_Buckets.S3_Buckets_Construct import S3BucketsConstruct

class MyProjectStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        s3_buckets = S3BucketsConstruct(self, "S3Buckets")