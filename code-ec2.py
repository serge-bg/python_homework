# Exercise
# Write a function to create an EC2 instance with the name ec2-created-by-python.
# - Provide an Amazon Linux 2 AMI
# - Use t3.micro instance type

# Use all the best practices, logging, handle exception, use variables, use main, doc strings etc…

#Operation and solution

# 1. Import Required Libraries
import boto3   
from botocore.exceptions import ClientError

#2. Initialize the EC2 client
def create_ec2_instance():
    """
    Creates an EC2 instance named ec2-created-by-python with 
    the following parameters (ImageId, instanceType, KeyName, MaxCount, 
    MinCount, SecurityGroupIds, SubnetId  ) and tags, including a 8 gbs volume.
    """
    ec2 = boto3.client('ec2')  

# 3. Define Parameters (Required)
    try:                                    
        response = ec2.run_instances(
            ImageId='ami-012967cc5a8c9f891',
            InstanceType='t2.micro',
            KeyName='jan2024class-key',
            MaxCount=1,
            MinCount=1,
            SecurityGroupIds=[
                'sg-000283cff4004abc0',
            ],
            SubnetId='subnet-0225587e50bc02d3f',

 # 4. Configure Block Device Mappings
            BlockDeviceMappings=[          
            {
                'DeviceName': '/dev/sda1',  # Device name
                'Ebs': {
                    'DeleteOnTermination': True,
                    'VolumeSize': 8,
                    'VolumeType': 'gp3',
                    'Encrypted': True
                },
            },
        ],

# 5. Tags for the Instance
        TagSpecifications=[
            {
                'ResourceType': 'instance',
                'Tags': [
                    {
                        'Key': 'Name',
                        'Value': 'ec2-created-by-python'
                    },
                ]
            },
        ],  
        )
        instance_id = response['Instances'][0]['InstanceId']
        print(f"Instance {instance_id} created successfully!")
        return {"InstanceId": instance_id}  # This should always be inside the function
    except ClientError as e:
        print(f"ClientError occurred: {e}")
        raise
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        raise

# 6. Execution Block
if __name__ == "__main__":
    create_ec2_instance()