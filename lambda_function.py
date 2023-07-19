import json
import smtplib
import boto3
import os
import random
import string
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import date
from constants import *


def generate_license_key(length):
    characters = string.ascii_uppercase + string.digits
    license_key = ''.join(random.choice(characters) for _ in range(length))
    return license_key


def create_new_license_key(email_address, license_key) -> bool:
    """
    Create a new license key and save it to the DynamoDB table. 
    Returns True if the creation is successful, False otherwise.
    """
    try:
        write_new_license_key(email_address, license_key, '')
        return True
    except:
        return False

    
def write_new_license_key(email_address, license_key, machine_id) -> bool:
    """
    Writes a new license key to the DynamoDB table. 
    Returns True if the write is successful, False otherwise.
    """
    try:
        SECRET_KEY = os.environ.get('SECRET_KEY')
        ACCESS_KEY = os.environ.get('ACCESS_KEY')
        REGION_NAME = os.environ.get('REGION_NAME')

        # Create a session with the AWS credentials
        session = boto3.Session(
            aws_access_key_id=ACCESS_KEY,
            aws_secret_access_key=SECRET_KEY,
            region_name=REGION_NAME
        )
        # Create a resource for DynamoDB
        dynamodb = session.resource('dynamodb')
        # Specify the table name
        table_name = "KonnectedReverseRaffleLicenseKeys"
        # Get the table
        table = dynamodb.Table(table_name)

        # Put the license key into the table
        table.put_item(
            Item={
                'Email': email_address,
                'LicenseKey': license_key,
                'MachineID': machine_id,
                'Created': date.today().strftime(DATE_FORMAT)
            }
        )
        return True
    except:
        return False

def create_html_markup(customer_name, license_key):
    html = f"""
        <html>
            <head>
                <style>
                    p {{
                        font-family: Arial, sans-serif;
                        font-size: 14px;
                    }}
                </style>
            </head>
            <body>
                <p>Hi {customer_name}!</p>
                <p>Here is your personal Konnected Reverse Raffle Licence key: {license_key}</p>
                <p>Please direct any queries you may have to reverse@justkonnect.com and we will do our best to get back to your promptly.</p>
                <p>Regards</p>
                <p>The Reverse Raffle Team</p>
            </body>
        </html>
    """
    return html


def create_email_body(customer_name, license_key):
    body_text = f"""
Hi {customer_name}!

Here is your personal Konnected Reverse Raffle Licence key: {license_key}
Please direct any queries you may have to reverse@justkonnect.com and we will do our best to get back to your promptly.

Regards
The Reverse Raffle Team
    """
    return body_text

    
def send_email(to, body_text, body_html):
    """This function is a helper function for Lambda Function
    that takes email address, subject and email message as 
    an argument and sends an email to the email address"""
    
    gmail_user = os.environ.get('GMAIL_USER')
    gmail_app_password = os.environ.get('GMAIL_APP_PASSWORD')

    sent_from = gmail_user
    subject = "License Key for Konnected Reverse Raffle Application"

    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', smtplib.SMTP_SSL_PORT)
        server.ehlo()
        server.login(gmail_user, gmail_app_password)
        
        msg = MIMEMultipart('alternative')
        msg['Subject'] = subject
        msg['From'] = sent_from
        msg['To'] = to
        
        # Record the MIME types of both parts - text/plain and text/html.
        part1 = MIMEText(body_text, 'plain')
        part2 = MIMEText(body_html, 'html')
        
        # Attach parts into message container.
        # According to RFC 2046, the last part of a multipart message, in this case
        # the HTML message, is best and preferred.
        msg.attach(part1)
        msg.attach(part2)
        
        server.sendmail(sent_from, to, msg.as_string())
        server.close()
        return "Successfully sent email!"
    except Exception as exception:
        return "Error: %s!\n\n" % exception


def lambda_handler(event, context):
    try:
        if type(event) == str:
            body = json.loads(event).get('body', {})
            if type(body) == str:
                body = json.loads(body)
        elif type(event) == dict:
            body = event.get('body', {})
            if type(body) == str:
                body = json.loads(body)
        
        body = body.get('data', body)
        contact_email = body.get('contact_email', 'gtahir1326@gmail.com')
        customer_name = body.get('customer_name', 'Customer')
        license_key = generate_license_key(12)
        create_new_license_key(contact_email, license_key)
        
        body_html = create_html_markup(customer_name, license_key)
        body_text = create_email_body(customer_name,  license_key)
        
        status_message = send_email(contact_email, body_text, body_html)
        return {
                'statusCode': 200,
                'body': json.dumps(status_message)
                }       

    except Exception as e:
        
        send_email("gtahir1326@gmail.com", f"{str(e)}", f"BODY: {body} \n\nERROR: {str(e)}")
        return {
           'statusCode': 404,
           'body': json.dumps(f"Error: unable to send email {e}")
              }
          