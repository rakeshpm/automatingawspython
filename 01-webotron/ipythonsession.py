import boto3
session = boto3.Session(profile_name='pythonAutomation')
s3 = session.resource('s3')

new_bucket = s3.create_bucket(Bucket='boto3bucket-therakeshpm')
ec2_client = session.client('ec2')
