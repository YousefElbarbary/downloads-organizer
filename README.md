## Purpose
Automatically scans and organizes files in a directory into folders and subfolders based on their file type.



## Plan for version v0.1

- Scan a file directory.
- Create category folders if not present.
- Identify files by their extension based on the list below.
- Ignore directories in v0.1.
- Periodically scan the downloads folder.
- Move all uncategorized files into their specific folder.
- Any extension not mentioned below should go into the others folder.
- Handle duplicate file names. (rename)
- Handle extension capitalization.

## Extension goals (can be pushed to v0.2)
- Handle files being processed (downloading or being actively edited).


## Folder categories and extensions planned for v0.1

Downloads/ 
{
	Media/
	{
		Images/ (JPEG, JPG, GIF, PNG, SVG)
		Audio/ (MP3, WAV, AAC)
		Video/ (MP4, MOV, MKV, AVI, WEBM)
		
	}

	Documents/
	{
		PDFs/ (PDF, EPUB)
		Office/ (DOCX, DOC, XLS, XLSX, CSV, PPT, PPTX)
		Text/ (TEXT, MD)
	}
	Archives/ (ZIP, RAR, 7Z, TAR, GZ, ISO)
	
	Applications/ (EXE)

	Others/ (mysterious extensions, failed moves and no extensions)

}

Note: Will be expanded further in future versions
