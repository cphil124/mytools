import requests
from io import open as iopen
import os
import torch
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

def get_img_normalize_mean(device='cpu'):
    if device == 'cpu':
        return torch.tensor([0.485, 0.456, 0.406])
    elif device == 'cuda':
        return torch.tensor([0.485, 0.456, 0.406]).to(device)

def get_img_normalize_std(device='cpu'):
    if device == 'cpu':
        return torch.tensor([0.229, 0.224, 0.225])
    elif device == 'cuda':
        return torch.tensor([0.229, 0.224, 0.225]).to(device)
