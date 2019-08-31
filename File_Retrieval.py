import requests
from io import open as iopen
import os
from urllib.parse import urlsplit

def requests_image(file_url):
    suffix_list = ['jpg', 'png', 'gif']
    file_name = urlsplit(file_url)[2].split('/')[-1]
    file_suffix = file_name.split('.')[-1]
    i = requests.get(file_url)
    if file_suffix in suffix_list and not os.path.exists('.\\'+file_name):
        with iopen(file_name, 'wb') as f:
            f.write(i.content)
    else:
        return False

