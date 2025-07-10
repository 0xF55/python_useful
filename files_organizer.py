import shutil # to copy the files
import threading # for making threads and better speed
import os # for listing,...
print("$File Organizer\nBy 0xF55")

def organize(ext: str,files) -> None:
    
    org_file = "{}{}".format(ext,"_files")

    try:
        if not os.path.exists(org_file):
            os.mkdir(org_file,mode=666)
        
        print("Working on",org_file)
        for file in files:
            if file.split(".")[-1] == ext:
                print(file)
                shutil.move(file,os.path.join(org_file,file))
                
    except Exception as e:
        print(e)
        

def main():
    l_files = os.listdir()
    files = []
    for f in l_files:
        if os.path.isfile(f):
            files.append(f)
    if not files:
        print("Folder is empty")
        os._exit(0)
    print(files)    
    for file in files:
        ext = file.split(".")[-1]
        organize(ext,files)
    
if __name__ == '__main__':
    main()
