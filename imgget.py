import requests
from io import open as iopen
import os
from urllib.parse import urlsplit

def requests_image(file_url):
    suffix_list = ['jpg', 'png', 'gif']
    file_name = urlsplit(file_url)[2].split('/')[-1]
    file_suffix = file_name.split('.')[-1]
    i = requests.get(file_url)
    file_path = ''
    if file_suffix in suffix_list:
        if not os.path.exists('.\\'+file_name):
            with iopen(file_name, 'wb') as f:
                f.write(i.content)
                file_path = f.name
        else: 
            file_path = os.path.abspath('.\\'+file_name)
        
        return file_path
    else:
        return False

def get_url_file_title(file_url):
    return urlsplit(file_url)[2].split('/')[-1].split('.')[0]

def get_url_filename(file_url):
    return urlsplit(file_url)[2].split('/')[-1]