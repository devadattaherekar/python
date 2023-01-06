import boto3


aws_console=boto3.session.Session(profile_name="s3_developer")
print("using resource to list buckets")
s3_console=aws_console.resource('s3')
for bucket in s3_console.buckets.all():
    print(bucket.name)

aws_console=boto3.session.Session(profile_name="s3_developer")
print("using client to list buckets")
s3_console=aws_console.client('s3')
for bucket in s3_console.list_buckets()['Buckets']:
    print(bucket['Name'])