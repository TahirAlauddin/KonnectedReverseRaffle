import winreg
import requests
import wmi
import json
import re
import os
from PyQt5.QtCore import *
import boto3
from dotenv import load_dotenv

load_dotenv()


CONFIG_FILE = 'config.json'

def validate_email_address(email_address):
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    # pass the regular expression
    # and the string into the fullmatch() method
    if(re.fullmatch(regex, email_address)):
        return True
    return False
 

def is_internet_connected():
    """
    Checks if the computer is connected with internet
    Returns True if it is connected, otherwise returns False
    """
    try:
        requests.get('https://google.com')
        return True
    except requests.exceptions.ConnectionError:
        return False

def get_license_key_from_config():
    config = json.load(open(CONFIG_FILE))
    return config.get('license_key')


def set_license_key_in_config(license_key):
    """Set the license key in config.yml file for future use"""
    with open(CONFIG_FILE) as config_file:
        config = json.load(config_file)

    config['license_key'] = license_key

    with open(CONFIG_FILE, 'w') as config_file:
        json.dump(config, config_file)

    
def get_machine_id():
    """
    This function retrieves the unique machine identifier of the computer where the code is executed.
    If the function is unable to retrieve the identifying number, it raises an exception with the message 
    "Couldn't get the Unique ID of this Machine!".
    """
    c = wmi.WMI()
    for item in c.Win32_ComputerSystemProduct():
        return item.IdentifyingNumber
    
    raise Exception("Couldn't get the Unique ID of this Machine!")

    
def create_new_license_key(email_address, license_key, dynamodbTable) -> bool:
    """
    Create a new license key and save it to the DynamoDB table. 
    Returns True if the creation is successful, False otherwise.
    """
    try:
        write_license_key(email_address, license_key, '', dynamodbTable)
        return True
    except:
        return False

    
def write_license_key(email_address, license_key, machine_id, dynamodbTable) -> bool:
    """
    Writes a new license key to the DynamoDB table. 
    Returns True if the write is successful, False otherwise.
    """
    try:
        # Put the license key into the table
        dynamodbTable.put_item(
            Item={
                'Email': email_address,
                'LicenseKey': license_key,
                'MachineID': machine_id
            }
        )
        return True
    except:
        return False

def license_key_is_valid(mainWindow, license_key, dynamodbTable) -> bool:
    """
    Checks if the provided license key is present in the DynamoDB table. 
    It also makes sure that the same license key is not being used in multiple computers.
    Returns True if it is present, False otherwise."""
    machine_id = get_machine_id()
    licenses = list_license_keys(dynamodbTable)
    license_keys = [license[0] for license in licenses.values()]
    emails = [email for email in licenses.keys()]
    if license_key in license_keys:
        lincense_key_idx = license_keys.index(license_key)
        email = emails[lincense_key_idx]
    else:
        # Invalid License Key
        return False

    if license_key in license_keys:
        machine_id_on_cloud = licenses[email][1]

        if machine_id_on_cloud:
            if machine_id_on_cloud == machine_id:
                # Valid License Key, being properly used
                return True
            # Cannot use same license key in multiple computers
            raise Exception("Cannot use same license key in multiple computers!")

        # New License key created but not used yet
        # Update machine_id for license_key
        write_license_key(email, license_key, machine_id, dynamodbTable)
        return True
    

def list_license_keys(dynamodbTable) -> dict:
    """
    Returns a list of all license keys present in the DynamoDB table.
    """
    # Use the scan method to get all items in the table
    response = dynamodbTable.scan()
    
    # Extract the license keys from the response
    license_keys = {item['Email']: [
                                    item.get('LicenseKey'),
                                    item.get('MachineID')
                                    ] for item in response['Items']}
    
    return license_keys


def get_dynamodb_table(table_name="KonnectedReverseRaffleLicenseKeys"):

    try:

        ACCESS_KEY = os.environ.get('KONNECTED_REVERSE_RAFFLE_ACCESS_KEY')
        SECRET_KEY = os.environ.get('KONNECTED_REVERSE_RAFFLE_SECRET_KEY')
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
        # Get the table
        table = dynamodb.Table(table_name)
        return table

    except Exception as e:
        return None


def get_file_size_mb(file_path):
    """
    Returns the size of the file in megabytes (MB)
    """
    if os.path.isfile(file_path):
        size_bytes = os.path.getsize(file_path)
        size_mb = size_bytes / (1024 * 1024)
        return size_mb
    else:
        return None



def get_themes_names():
    themes = get_themes()
    return list(themes.keys())


def get_themes():
    with open('themes.json') as themes_file:
        themes = json.load(themes_file)
    return themes


def get_number_of_rows(grid_size, columns_constant):
    if grid_size % columns_constant == 0:
        return grid_size // columns_constant
    else:
        return (grid_size // columns_constant) + 1



def get_users_desktop_folder():
    # Open the registry key for the desktop folder
    key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders")

    # Get the value of the "Desktop" key
    desktop_path = winreg.QueryValueEx(key, "Desktop")[0]

    return desktop_path
