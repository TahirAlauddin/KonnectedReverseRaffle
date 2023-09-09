from flask import Flask, request, jsonify, render_template, send_file
import os
import csv
import json
import base64
import pickle
import logging
from utils import (set_license_key_in_config, get_license_key_from_config,
                    get_dynamodb_table, license_key_is_valid)

# Configure the logging level
logging.basicConfig(level=logging.INFO)

# Get the logger for the current module
logger = logging.getLogger(__name__)

# Create a handler that writes log messages to a file
handler = logging.FileHandler('error.log')

# Create a formatter that specifies the format of the log messages
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

PORT = 8323

# For Production
# app = Flask(__name__,
#             static_folder='frontend/static/', static_url_path='/static/',
#             template_folder='frontend/templates')

# For Development
app = Flask(__name__,
            static_folder='../frontend/static/', static_url_path='/static/',
            template_folder='../frontend/templates')

base_path = os.path.join(app.root_path, 'frontend', 'media')

def remove_uploaded_background_images():
    import glob

    pattern = os.path.join(base_path, 'Background-Image*.png')

    # Using glob to find all matching files
    for file_path in glob.glob(pattern):
        if os.path.exists(file_path):
            os.remove(file_path)
            print(f"Removed: {file_path}")


@app.route('/admin/')
def view_admin_page():
    try:
        license_key = get_license_key_from_config()
        csv_file_path = os.path.join(app.root_path, 'participants.csv')
        if os.path.exists(csv_file_path):
            os.remove(csv_file_path)

        # Remove uploaded images
        remove_uploaded_background_images()

        return render_template('adminPage.html', license_key=license_key)
    except Exception as e:
        logger.error(e)
        print(e)
        # raise(e)
        return "An Error Occurred!"


@app.route('/home/')
def view_home_screen():
    try:
        pickle.dump(dict(request.args), open('admin_conf.pkl', 'wb'))
        return render_template('main.html')
    except Exception as e:
        print(e)
        logger.error(e)
        return 'An error occurred'


@app.route('/saveCSVData/', methods=['POST'])
def save_csv():
    try:
        if request.method == 'POST':
            csv_data = request.get_data()    
            # Decode the bytes to string
            csv_data_str = csv_data.decode('utf-8').replace('\\n', '\n').replace('\\r', '').strip('"').replace('\\', '').replace('\\\\','').replace('X', '')
            # Remove extra quotes
            csv_data_str = csv_data_str.replace('\"', '')
            # Split the string into a list of lines
            csv_data_lines = csv_data_str.splitlines()

            numbers = [line.split(',')[0] for line in csv_data_lines[1:]]
            names = [f"{line.split(',')[1]} {line.split(',')[2]}" for line in csv_data_lines[1:]]

            if len(set(numbers)) != len(numbers):
                return jsonify({"error": "All numbers provided in the table must be unique."}), 400

            # Numbers input handling
            for idx, number in enumerate(numbers):
                if not number:
                    return jsonify({"error": f"The number at [ROW # {idx + 1}] cannot be empty."}), 400

                if len(number) > 4:
                    return jsonify({"error": f"The length of {number} at [ROW # {idx + 1}] cannot be more than 4 letters."}), 400

                if not number.isdigit():
                    return jsonify({"error": f"{number} at [ROW # {idx + 1}] is not a valid digit/number."}), 400

            # NAMES must not be empty, input handling
            for idx, name in enumerate(names):
                if name == ' ':
                    return jsonify({"error": f"The name at [ROW # {idx + 1}] cannot be empty."}), 400


            new_csv_data_lines = []
            for line in csv_data_lines[1:]:
                line = line.rstrip(',')
                if line:
                    cell = line.split(',')[0]
                    if not cell.isdigit():
                        continue
                    new_csv_data_lines.append(line)

            csv_data_lines = new_csv_data_lines

            if len(csv_data_lines) < 50:
                return jsonify({"error": "Participants cannot be less than 50"}), 400

            if len(csv_data_lines) > 300:
                return jsonify({"error": "Participants cannot be more than 300"}), 400

            # Open a file in write mode
            with open('participants.csv', newline='', mode='w') as file:
                writer = csv.writer(file)

                # Write each line to the CSV file
                for line in csv_data_lines:
                    writer.writerow(line.split(','))

            return jsonify({"success": f"File has been saved at: participants.csv"})
        else:
            return jsonify({"error": "POST request required."}), 400
    except Exception as e:
        logger.error(e)
        return jsonify({'error': 'An error occurred'}), 500


@app.route('/getCSVData/')
def view_saved_csv():
    try:
        file_path = 'participants.csv'
        if os.path.exists(file_path):
            data_list = []
            with open(file_path, newline='') as f:
                csv_data = csv.reader(f)
                # headers = next(csv_data, None)  # returns the headers or `None` if the input is empty
                headers = ['assign-number', 'first-name', 'last-name', 'date-added']
                if headers:
                    for row in csv_data:
                        data_list.append({headers[i]: value for i, value in enumerate(row)})
                return jsonify({"data": data_list})
        else:
            return jsonify({"error": "File not found"}), 404
    
    except Exception as e:
        logger.error(e)
        return jsonify({'error': 'An error occurred'}), 500

@app.route('/getAdminConf/')
def get_admin_conf():
    try:
        obj = pickle.load(open('admin_conf.pkl', 'rb'))
        return jsonify(obj)
    except Exception as e:
        logger.error(e)
        return jsonify({'error': 'An error occurred'}), 500



@app.route('/saveImage/', methods=['POST'])
def save_image():
    try:
        if request.method == 'POST':
            data = json.loads(request.get_data(as_text=True))
            image_name = data.get('image_name', None)
            img_data = data['image'].split(',')[1]  # Split off the header, keep only the actual image content
            img_data = base64.b64decode(img_data)
            file_path = os.path.join(base_path, 'frontend', f'media', f'{image_name}.png')  # Or where you want to save it

            if image_name == 'Logo':
                file_path = os.path.join(fr'media\{image_name} Uploaded.png')  # Or where you want to save it

            elif image_name == None:
                # Background Image Uploaded
                file_path = get_image_path_name()

            with open(file_path, 'wb') as f:
                f.write(img_data)

            return jsonify({"message": "Image saved successfully.", 'file_path': file_path})
        else:
            return jsonify({"error": "Wrong method type."})

    except Exception as e:
        logger.error(e)
        return jsonify({'error': 'An error occurred'}), 500



@app.route('/validateLicenseKey/<string:licenseKey>/', methods=['POST'])
def view_validate_license_key(licenseKey):
    try:
        table = get_dynamodb_table()
        licenseCreatedDate = license_key_is_valid(licenseKey, table)
        # If license exists, write/update it to config file
        if licenseCreatedDate:
            set_license_key_in_config(licenseKey, licenseCreatedDate)
            return jsonify({'success': 'License Key successfully validated'}), 200
        return jsonify({'error': 'License Key couldn\'t be validated'}), 404

    except Exception as e:
        from traceback import print_exc
        logger.error(e)
        print_exc()
        return jsonify({'error': str(e)}), 500


@app.route('/licenseKeyIsValid/')
def view_license_key_validated():
    license_key = get_license_key_from_config()
    if license_key:
        return jsonify({'success': 'License Key is validated!'}), 200
    return jsonify({'error': 'Please enter a valid License Key in order to use this software.'}), 400


@app.route('/media/<filename>')
def get_media_file(filename):
    return send_file(os.path.join('../frontend', 'media', filename))



def get_image_path_name():
    # Background Image Uploaded
    file_name = 'Background-Image'
    extension = '.png'
    counter = 0

    # Loop to find the next available file name
    while True:
        if counter == 0:
            file_path = os.path.join(base_path, f'{file_name}{extension}')
        else:
            file_path = os.path.join(base_path, f'{file_name} {counter}{extension}')

        # Check if file already exists
        if not os.path.exists(file_path):
            break # Exit loop if file does not exist

        counter += 1

    return file_path



if __name__ == "__main__":
    app.run(port=PORT)
