import boto3


aws_console=boto3.session.Session(profile_name="iam_user")
iam_console=aws_console.resource("iam")
#print(dir(iam_console))
print("using resource to display IAM users")
print(iam_console.users.all()) # resource returns an object
for user in iam_console.users.all():
    print(user.name)
print("____________________")
print("using client to display IAM users")
iam_console=aws_console.client("iam")
response=iam_console.list_users()
#print(response["Users"])
for user in response["Users"]:
    print(user["UserName"])