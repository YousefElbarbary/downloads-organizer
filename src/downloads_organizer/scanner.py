from pathlib import Path, WindowsPath

def scan(folder_dir):
    files = []

    for file in folder_dir.glob('*'):
        if file.is_file():
            files.append(file)
    
    return(files)