from pathlib import Path, WindowsPath

def move(src_path, dest_path):
    src_path.rename(dest_path)

def check_dir_exists (dest_path):
    dest_path.mkdir(parents = True, exist_ok = True)

def check_dup_name(src, dest_path):
    dest_path = dest_path/ src.name
    counter = 1
    stem = dest_path.stem
    parent = dest_path.parents[0]
    suffix = dest_path.suffix
    while dest_path.exists():
        dest_path = parent / f"{stem} ({counter}){suffix}"
        counter+=1
    return(dest_path)


def organize(src, dest):
    check_dir_exists(dest)
    modified_dest = check_dup_name(src, dest)
    move(src,modified_dest)
