from django.views.decorators.csrf import csrf_exempt
from django.urls import path
from django.shortcuts import render
from django.conf import settings
from django.conf.urls.static import static
from django.http import JsonResponse, HttpResponse
import csv
import os
import pickle
import json, base64
from .utils import (set_license_key_in_config, get_license_key_from_config,
                    get_dynamodb_table, license_key_is_valid)
import logging

logger = logging.getLogger(__name__)


def view_license_key_validated(request):
    license_key = get_license_key_from_config()
    if license_key:
        return JsonResponse({'success': 'License Key is validated!'}, status=200)
    return JsonResponse({'error': 'Please enter a valid License Key in order to use this software.'}, status=400)

def view_validate_license_key(request, licenseKey):
    try:
        table = get_dynamodb_table()
        licenseCreatedDate = license_key_is_valid(licenseKey, table)
        # If license exists, write/update it to config file
        if licenseCreatedDate:
            set_license_key_in_config(licenseKey, licenseCreatedDate)
            return JsonResponse({'success': 'License Key successfully validated'}, status=200)
        return JsonResponse({'error': 'License Key couldn\'t be validated'}, status=400)

    except Exception as e:
        from traceback import print_exc
        logger.error(e)
        print_exc()
        return JsonResponse({'error': str(e)}, status=500)

def get_admin_conf(request):
    try:
        obj = pickle.load(open('admin_conf.pkl', 'rb'))
        return JsonResponse(obj)
    except Exception as e:
        logger.error(e)
        return JsonResponse({'error': 'An error occurred'}, status=500)

def view_saved_csv(request):
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
                return JsonResponse({"data": data_list})
        else:
            return JsonResponse({"error": "File not found"}, status=404)
    
    except Exception as e:
        logger.error(e)
        return JsonResponse({'error': 'An error occurred'}, status=500)

@csrf_exempt
def save_csv(request):
    try:
        if request.method == 'POST':
            csv_data = request.body    
            # Decode the bytes to string
            csv_data_str = csv_data.decode('utf-8').replace('\\n', '\n').replace('\\r', '').strip('"').replace('\\', '').replace('\\\\','').replace('X', '')
            # Remove extra quotes
            csv_data_str = csv_data_str.replace('\"', '')
            # Split the string into a list of lines
            csv_data_lines = csv_data_str.splitlines()

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
                return JsonResponse({"error": "Participants cannot be less than 50"}, status=400)

            # Open a file in write mode
            with open('participants.csv', newline='', mode='w') as file:
                writer = csv.writer(file)

                # Write each line to the CSV file
                for line in csv_data_lines:
                    writer.writerow(line.split(','))

            return JsonResponse({"success": f"File has been saved at: participants.csv"})
        else:
            return JsonResponse({"error": "POST request required."}, status=400)
    except Exception as e:
        logger.error(e)
        return JsonResponse({'error': 'An error occurred'}, status=500)

@csrf_exempt
def save_image(request):
    try:
        if request.method == 'POST':
            data = json.loads(request.body)
            image_name = data['image_name']
            img_data = data['image'].split(',')[1]  # Split off the header, keep only the actual image content
            img_data = base64.b64decode(img_data)
            file_path = os.path.join(settings.BASE_DIR, f'media/{image_name}.png')  # Or where you want to save it

            with open(file_path, 'wb') as f:
                f.write(img_data)

            return JsonResponse({"message": "Image saved successfully."})
        else:
            return JsonResponse({"error": "Wrong method type."})

    except Exception as e:
        logger.error(e)
        return JsonResponse({'error': 'An error occurred'}, status=500)


def view_home_screen(request):
    try:
        pickle.dump(dict(request.GET), open('admin_conf.pkl', 'wb'))
    except Exception as e:
        logger.error(e)
        return HttpResponse('An error occured')
    return render(request, 'main.html', )


def view_admin_page(request):
    try:
        license_key = get_license_key_from_config()
        csv_file_path = os.path.join(settings.BASE_DIR, 'participants.csv')
        if os.path.exists(csv_file_path):
            os.remove(csv_file_path)
        return render(request, 'adminPage.html', context={'license_key': license_key})
    except Exception as e:
        logger.error(e)
        return HttpResponse("An Error Occured!")


urlpatterns = [
    path('admin/', view_admin_page),
    path('home/', view_home_screen),
    path('saveCSVData/', save_csv),
    path('getCSVData/', view_saved_csv),
    path('getAdminConf/', get_admin_conf),
    path('savePrizeImage/', save_image),
    path('validateLicenseKey/<str:licenseKey>/', view_validate_license_key),
    path('licenseKeyIsValid/', view_license_key_validated),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) 

urlpatterns += static(settings.MEDIA_URL, 
document_root=settings.MEDIA_ROOT)
