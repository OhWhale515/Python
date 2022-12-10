#--List Bucket Names--
import boto3
from botocore.exceptions import ClientError
s3_client = boto3.client('s3')

s3 = boto3.resource('s3')
buckets = s3.buckets.all()
for bucket in buckets:
    print(bucket)
 
print()

#--Create Bucket--
import boto3
#from botocore.exceptions import ClientError
s3.create_bucket(Bucket='pyproz')

print()

#--Updated Bucket List--    
import boto3
client = boto3.client('s3')
response = client.list_buckets()
for bucket in response['Buckets']:
    print(bucket['Name'])

print()

#--Delete Bucket--    
import boto3
s3 = boto3.resource('s3')
bucket = s3.Bucket('pyproz')
bucket.delete()

print()

#--Updated Bucket List w/ ARN-- 
import boto3
client = boto3.client('s3')
response = client.list_buckets()
for bucket in response['Buckets']:
    print(bucket['Name'])
    
    
print() 



#response = client.list_bucket_metrics_configurations(
#    Bucket='projecthandz',
    #ContinuationToken='arn:aws:s3:::apachework',
#    ExpectedBucketOwner='558725381699'
#)

#print()

#response = client.list_bucket_metrics_configurations(
#    Bucket='projectslim',
    #ContinuationToken='string',
#    ExpectedBucketOwner='558725381699'
#)

#print()

#response = client.list_bucket_metrics_configurations(
#    Bucket='slgbucketslim',
    #ContinuationToken='string',
#    ExpectedBucketOwner='558725381699'
#)

#print()

#response = client.list_bucket_metrics_configurations(
#    Bucket='test-bucket-989282',
    #ContinuationToken='string',
#    ExpectedBucketOwner='558725381699'
#)

#print()

#response = client.list_bucket_metrics_configurations(
#    Bucket='string',
#    ContinuationToken='string',
#    ExpectedBucketOwner='string'
#)

