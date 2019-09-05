
# This file formerly titled file_explorer_select.py

import tkinter as tk
from tkinter import filedialog
import os
from shutil import copy2
import mytools.imgget

def _setup_root():
    root = tk.Tk()
    root.withdraw()

def choose_folder(title=None):
    _setup_root()
    directory = filedialog.askdirectory(title=title)
    return directory

def choose_file_name(title=None):
    """
    Opens a tkinter file select window. After selecting a file, 
    the function returns an absolute path to that file in the system.
    """
    _setup_root()
    filepath = filedialog.askopenfilename(title=title)
    return filepath

def choose_file_names(title=None):
    """
    Opens a tkinter file select window. After selecting files, 
    the function returns a list of absolute paths to those files in the system.
    """
    _setup_root()
    filepaths = []
    filepaths.append(filedialog.askopenfilenames(title=title))
    return filepaths

def choose_file(title=None):
    """
    Returns an io wrapper object pointing towards that file in the system.
    Can be used as a user-select open() function
    """
    _setup_root()
    filepath = filedialog.askopenfile(title=title)
    return filepath

def choose_files(title=None):
    """
    Returns a list containing io wrapper objects pointing towards the selected files in the system.
    """
    _setup_root()
    files = []
    files.append(filedialog.askopenfiles(title=title))
    return files

def copy_all_to_dir(path_list, dir=os.getcwd()):
    path_list = []
    for path in path_list:
        new_path = copy2(path, dir)
        path_list.append(new_path)
    return path_list


def make_im_dir():
    if 'images' not in os.listdir():
        os.mkdir('images')
    os.chdir('images')
    im_dir = os.path.abspath(os.getcwd()) 
    os.chdir('..')
    return im_dir