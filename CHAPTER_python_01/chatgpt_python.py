import os
#use the os module to list the diretory content 
# select the directory whose content want to lest
def print_only_files(path='/New folder'):
    try:
        entries = os.listdir(path)
    except OSError as e:
        print(f"Error: {e}")
        return

    for name in entries:
        full = os.path.join(path, name)
        if os.path.isfile(full):  # filter only files :contentReference[oaicite:1]{index=1}
            print(name)
