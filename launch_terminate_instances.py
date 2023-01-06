import boto3
import sys

aws_con=boto3.session.Session(profile_name="ec2_developer")

ec2_con_cl=aws_con.client(service_name="ec2",region_name="us-east-1")

while True:
    print("1.start 2.stop 3.terminate 4.exit on ec2 instance\n")
    choice=int(input("Enter your choice: "))
    if choice==1:
        instance_id=input("Enter instance Id ")
        # resource acts on single instances at a time
        # client will operate on a list of instance_ids
        ec2_con_cl.start_instances(InstanceIds=[instance_id])
        print("Starting ec2 instance")
    elif choice==2:
        instance_id=input("Enter instance Id ")
        ec2_con_cl.stop_instances(InstanceIds=[instance_id])
        print("Stoping ec2 instance")
    elif choice==3:
        print("Terminating ec2 instance")
        instance_id=input("Enter instance Id ")
        ec2_con_cl.terminate_instances(InstanceIds=[instance_id])
    elif choice==4:
        sys.exit()
    else:
        print("Invalid option")
