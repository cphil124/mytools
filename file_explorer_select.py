import tkinter as tk

def _setup_root():
    root = tk.Tk()
    root.withdraw()

def choose_folder():
    _setup_root()
    directory = tk.filedialog.askdirectory()
    return directory

def choose_file_name():
    _setup_root()
    filepath = tk.filedialog.askopenfilename()
    return filepath

def choose_file_names():
    _setup_root()
    filepaths = []
    filepaths.append(tk.filedialog.askopenfilenames())
    return filepaths

def choose_file():
    _setup_root()
    filepath = tk.filedialog.askopenfile()
    return filepath

def choose_files():
    _setup_root()
    files = []
    files.append(tk.filedialog.askopenfiles())
    return files