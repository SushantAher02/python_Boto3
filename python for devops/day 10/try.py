# number = float(input("enter the number: "))  # or int(input(...)) for integers
# print(number)

# import os
# folders=input("Please provide list of  folder names with spaces in between: ").split()
# print(folders)

# for folder in folders:
#     try:
#        files = os.listdir(folder)
       
#     except FileNotFoundError:
#        print("Please a valid folder name, looks like this folder does not exit: "+ folder)
#        continue
#    except PermissionError:
#         print("No access this folder: "+ folder)
        
#    except ZeroDivisionError:
#        continue
   
#    print("===listing files for the folder -", + folder)
#    for file in files():
#        print(file)

import os

def list_files_in_folder(folder_path):
    try:
        files = os.listdir(folder_path)
        return files, None
    except FileNotFoundError:
        return None, "Folder not found"
    except PermissionError:
        return None, "Permission denied"

def main():
    folder_paths = input("Enter a list of folder paths separated by spaces: ").split()
    
    for folder_path in folder_paths:
        files, error_message = list_files_in_folder(folder_path)
        if files:
            print(f"Files in {folder_path}:")
            for file in files:
                print(file)
        else:
            print(f"Error in {folder_path}: {error_message}")

if __name__ == "__main__":
    main()
