import threading
import json
from datetime import datetime, timedelta
from constants import DATE_FORMAT, LICENSE_KEY_VALIDATION_LIMIT

class LicenseExpiryThread(threading.Thread):
    def __init__(self, window, expiry_days):
        super().__init__()
        self.expiry_days = expiry_days
        self.window = window

    def run(self):
        if self.is_license_expired():
            print("License expired!")
            # Add your code to handle the software closure or display an appropriate message to the user
            self.window.licenseExpired.emit()

    def is_license_expired(self):
        # Read the config.json file
        with open('config.json') as file:
            config_data = json.load(file)
        
        # Get the 'Created' value from the config data
        created_value = config_data.get('license_key_created')

        # Check if the 'license_key_created' value is present and older than the specified number of days
        if created_value:
            expiry_date = datetime.strptime(created_value, DATE_FORMAT) + timedelta(days=self.expiry_days)
            return expiry_date < datetime.today() 

        return False


if __name__ == '__main__':
    # Usage example
    expiry_thread = LicenseExpiryThread(LICENSE_KEY_VALIDATION_LIMIT)
    expiry_thread.start()
