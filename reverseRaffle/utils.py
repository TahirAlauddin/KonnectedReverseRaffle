# from PyQt5.QtCore import *
from dotenv import load_dotenv
import requests
import json
import re
import boto3
import os
import subprocess
import platform
from constants import *
from datetime import datetime, timedelta


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


def set_license_key_in_config(license_key, licenseCreatedDate):
    """Set the license key in config.yml file for future use"""
    with open(CONFIG_FILE) as config_file:
        config = json.load(config_file)

    config['license_key'] = license_key
    config['license_key_created'] = licenseCreatedDate

    with open(CONFIG_FILE, 'w') as config_file:
        json.dump(config, config_file)

    
def delete_license_key_in_config():
    """Delete the license key in config.yml file for future use"""
    with open(CONFIG_FILE) as config_file:
        config = json.load(config_file)

    config['license_key'] = None
    config['license_key_created'] = None

    with open(CONFIG_FILE, 'w') as config_file:
        json.dump(config, config_file)



def get_machine_id():
    """
    This function retrieves the unique machine identifier of the computer where the code is executed.
    If the function is unable to retrieve the identifying number, it raises an exception with the message 
    "Couldn't get the Unique ID of this Machine!".
    """
    # Detecting the OS
    current_os = platform.system().lower()

    # For Windows
    if current_os == 'windows':
        try:
            import pythoncom
            pythoncom.CoInitializeEx(pythoncom.COINIT_APARTMENTTHREADED)
            import wmi
            c = wmi.WMI()
            for item in c.Win32_ComputerSystemProduct():
                return item.IdentifyingNumber
        except ImportError:
            raise Exception("The wmi module is not installed. Please install it by running 'pip install wmi'.")

    # For MacOS
    elif current_os == 'darwin':
        try:
            uuid = subprocess.check_output("ioreg -rd1 -c IOPlatformExpertDevice | awk '/IOPlatformUUID/ { split($0, line, \"\\\"\"); printf(\"%s\\n\", line[4]); }'", shell=True).strip().decode()
            return uuid
        except:
            raise Exception("Couldn't get the Unique ID of this Machine!")

    # For Linux
    elif current_os == 'linux':
        try:
            uuid = subprocess.check_output(['cat', '/var/lib/dbus/machine-id']).strip().decode()
            return uuid
        except:
            raise Exception("Couldn't get the Unique ID of this Machine!")

    # For other OS
    else:
        raise Exception("Unsupported OS")


    
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
                'MachineID': machine_id,
                'Created': datetime.today().strftime(DATE_FORMAT),
            }
        )
        return True
    except:
        return False
    
# def mydecorator(func, *args, **kwargs):
#     print(args)
#     result = func(*args, **kwargs)
#     if len(result) == 2:
#         return result[0], result[1]
#     return result, None

# @mydecorator
def license_key_is_valid(license_key, dynamodbTable) -> bool:
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
        license_key_generated_date = licenses[email][2]

        if machine_id_on_cloud:
            # Logic for one license key on one machine
            if machine_id_on_cloud == machine_id:
                # Logic for License key 2 months expiration 
                if datetime.strptime(license_key_generated_date, 
                                     DATE_FORMAT) + timedelta(
                    days=LICENSE_KEY_VALIDATION_LIMIT) > datetime.today():
                    # Valid License Key, being properly used
                    return license_key_generated_date
                # Cannot use same license key after LICENSE_KEY_VALIDATION_LIMIT 
                raise Exception(LICENSE_KEY_EXPIRED_MESSAGE)

            # Cannot use same license key in multiple computers
            raise Exception("Cannot use same license key in multiple computers!")
        # New License key created but not used yet
        # Update machine_id for license_key
        if write_license_key(email, license_key, machine_id, dynamodbTable):
            print('Successfully saved Machine ID')
        else:
            print('Couldn"t save machine ID')
        return license_key_generated_date
    

def list_license_keys(dynamodbTable) -> dict:
    """
    Returns a list of all license keys present in the DynamoDB table.
    """
    # Use the scan method to get all items in the table
    response = dynamodbTable.scan()
    
    # Extract the license keys from the response
    license_keys = {item['Email']: [
                                    item.get('LicenseKey'),
                                    item.get('MachineID'),
                                    item.get('Created'),
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
    if os.name == 'nt':
        import winreg

        # Open the registry key for the desktop folder
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders")

        # Get the value of the "Desktop" key
        desktop_path = winreg.QueryValueEx(key, "Desktop")[0]

        return desktop_path
    else:
        return os.path.join(os.path.expanduser("~"), "Desktop")


def check_font_exists(font):
    if os.name == 'nt' or platform.system() == 'Windows':
        # Windows
        font_path = os.path.join(os.environ['WINDIR'], 'Fonts', font + '.ttf')
        return os.path.isfile(font_path)
    elif os.name == 'posix' or platform.system() == 'Darwin':
        # macOS
        font_dir = os.path.expanduser('~/Library/Fonts')
        font_path = os.path.join(font_dir, font + '.ttf')
        return os.path.isfile(font_path)
    else:
        # Unsupported OS
        return False


    
def load_font(font_path):
    from PyQt5.QtGui import QFontDatabase, QFont
    from PyQt5.QtWidgets import QApplication
    font_id = QFontDatabase.addApplicationFont(f':/fonts/{font_path}')
    font_families = QFontDatabase.applicationFontFamilies(font_id)
    if font_families:
        font_family = font_families[0]
        font = QFont(font_family)
        QApplication.setFont(font)
