import boto3
client = boto3.client('s3')

# response = client.create_bucket(
#     Bucket='sushantbhauchabucket1',
# )

#To see acl bucket list 
response = client.get_bucket_acl(
    Bucket='sushantbhauchabucket1'  
)
print(response)