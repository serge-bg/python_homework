#HOMEWORK - EXERCISE
# 
#  Repurpose the list_all_ec2_instances() to return a dictionary containing keyname: instance_name, instance_type, image_id, state
# 2. repurpose generate_csv_report to use DictWriter method
# 3. write a function to email yourself and CC cloudspace at info@cloudspaceacademy.com. If possible attach the report or send the s3 bucket link. Use AWS services
# CODE: https://dpaste.com/HUK88AY3F (edited) 

#I. Operation
import boto3
import botocore
import csv
import logging
import os
import base64
from botocore.exceptions import ClientError

# Setup loggers
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

# Global variables
REPORT_NAME = 'ec2_report.csv'
SENDER_EMAIL = 'sergebouopda@gmail.com'
RECIPIENTS = ['serge.bouopdaguechou@gmail.com']
AWS_REGION = 'us-east-1'


def list_of_my_ec2_instances():
    """
    Retrieve a dictionary of all EC2 instances with key details.

    :return: A list of dictionaries, each representing an EC2 instance.
    """
    ec2_client = boto3.client('ec2')
    list_of_ec2_instances = []

    # Retrieve the list of instances
    response = ec2_client.describe_instances()

    # Looping through the reservations
    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            instance_details = {
                "instance_name": next(
                    (tag['Value'] for tag in instance.get('Tags', []) if tag['Key'] == 'Name'),
                    "N/A"
                ),  # Extract name tag
                "instance_type": instance.get('InstanceType', "N/A"),
                "image_id": instance.get('ImageId', "N/A"),
                "state": instance['State']['Name'] if 'State' in instance else "N/A"
            }
            list_of_ec2_instances.append(instance_details)
    return list_of_ec2_instances


def generate_csv_report(instances):
    """
    This function will generate a CSV report.
    :param instances: list of EC2 instances
    :return: None
    """
    try:
        with open(REPORT_NAME, 'w', newline='') as csvfile:
            fieldnames = ['instance_name', 'instance_type', 'image_id', 'state']
            csvwriter = csv.DictWriter(csvfile, fieldnames=fieldnames)
            csvwriter.writeheader()
            csvwriter.writerows(instances)
    except OSError as error:
        logger.error(f'File was not found! {error}')


def upload_report_to_s3():
    """
    This function will upload the CSV report to an S3 bucket.
    """
    s3_client = boto3.client('s3')
    try:
        s3_client.upload_file(REPORT_NAME, 'ec2-upload-in-bucket', REPORT_NAME)
    except botocore.exceptions.ClientError as error:
        logger.error(f"Something happened while uploading the file {error}")


def email_report_with_attachment():
    """
    Function to send the generated report as an email attachment.
    """
    ses_client = boto3.client('ses', region_name=AWS_REGION)

    SUBJECT = "EC2 Instances Report"
    BODY_TEXT = "Dear Mr. Claudio,\n\nI hope this email finds you well.\n\nPlease find attached a CSV report containing the list of my EC2 instances. I would appreciate your feedback on any actions that may need to be undertaken.\n\nLooking forward to your response.\n\nBest regards,\nSerge Bouopda"
    CHARSET = "UTF-8"

    # Read the file to attach
    try:
        with open(REPORT_NAME, 'rb') as file:
            file_data = file.read()
            attachment_name = os.path.basename(REPORT_NAME)
    except FileNotFoundError:
        logger.error(f"File {REPORT_NAME} not found. Ensure the report is generated before emailing.")
        return False

    # Base64 encode the attachment data
    attachment_data = base64.b64encode(file_data).decode()

    # MIME format for email with attachment
    BOUNDARY = "NextPart"
    RAW_EMAIL = f"""From: {SENDER_EMAIL}
To: {", ".join(RECIPIENTS)}
Subject: {SUBJECT}
MIME-Version: 1.0
Content-Type: multipart/mixed; boundary="{BOUNDARY}"

--{BOUNDARY}
Content-Type: text/plain; charset="{CHARSET}"
Content-Transfer-Encoding: 7bit

{BODY_TEXT}

--{BOUNDARY}
Content-Type: text/csv; name="{attachment_name}"
Content-Disposition: attachment; filename="{attachment_name}"
Content-Transfer-Encoding: base64

{attachment_data}
--{BOUNDARY}--
"""

    # Sending email
    try:
        response = ses_client.send_raw_email(
            Source=SENDER_EMAIL,
            Destinations=RECIPIENTS,
            RawMessage={'Data': RAW_EMAIL}
        )
        logger.info(f"Email sent successfully! Message ID: {response['MessageId']}")
    except ClientError as error:
        logger.error(f"Failed to send email: {error}")
        return False
    return True


# Main function
if __name__ == "__main__":
    # Call the function to get instances
    instances = list_of_my_ec2_instances()
    logger.info(f'Generating CSV report {REPORT_NAME}')

    # Generate report
    generate_csv_report(instances)

    logger.info(f'Uploading report to S3')
    # Upload report
    upload_report_to_s3()

    logger.info(f'Sending email with attachment to {RECIPIENTS}')
    # Email report
    email_report_with_attachment()

    logger.info(f'Good night folks!!!')
