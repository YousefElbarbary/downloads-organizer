from pathlib import Path, WindowsPath

def classify(file_path, dict_paths):
    suffix = file_path.suffix.lower()

    output_directory = dict_paths.get(suffix)
    if output_directory is not None:
        return(output_directory)
    else:
        return(dict_paths[None])
