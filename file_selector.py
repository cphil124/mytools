
# This file formerly titled file_explorer_select.py

import tkinter as tk
from tkinter import filedialog

def _setup_root():
    root = tk.Tk()
    root.withdraw()

def choose_folder(title=None):
    _setup_root()
    directory = tk.filedialog.askdirectory(title=title)
    return directory

def choose_file_name(title=None):
    """
    Opens a tkinter file select window. After selecting a file, 
    the function returns an absolute path to that file in the system.
    """
    _setup_root()
    filepath = tk.filedialog.askopenfilename(title=title)
    return filepath

def choose_file_names(title=None):
    """
    Opens a tkinter file select window. After selecting files, 
    the function returns a list of absolute paths to those files in the system.
    """
    _setup_root()
    filepaths = []
    filepaths.append(tk.filedialog.askopenfilenames(title=title))
    return filepaths

def choose_file(title=None):
    """
    Returns an io wrapper object pointing towards that file in the system.
    Can be used as a user-select open() function
    """
    _setup_root()
    filepath = tk.filedialog.askopenfile(title=title)
    return filepath

def choose_files(title=None):
    """
    Returns a list containing io wrapper objects pointing towards the selected files in the system.
    """
    _setup_root()
    files = []
    files.append(tk.filedialog.askopenfiles(title=title))
    return files