from pathlib import Path, WindowsPath
from downloads_organizer.classifier import classify
from downloads_organizer.config import load_config
from downloads_organizer.organizer import organize
from downloads_organizer.scanner import scan

def main():
    downloads_folder = Path("D:/") / "Projects" / "downloads-organizer" / "tests"
    
    extension_map = load_config()
    files = scan(downloads_folder)
    
    for file in files:
        out_dir = classify(file, extension_map)
        out_dir = downloads_folder / out_dir
        organize(file,out_dir)

main()