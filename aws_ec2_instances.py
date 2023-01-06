import boto3


aws_console=boto3.session.Session(profile_name="ec2_developer")
print("using resource to list ec2 instances")
ec2_console=aws_console.resource('ec2')
for instance in ec2_console.instances.all():
    print(instance.id)

print("using client to list ec2 instances")
aws_console=boto3.session.Session(profile_name="ec2_developer")
ec2_console=aws_console.client('ec2')
for instance in ec2_console.describe_instances()['Reservations']:
    for ec2_instance in instance['Instances']:
        print(ec2_instance["InstanceId"])
