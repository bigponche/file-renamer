from requirements import NUMBER_DIGITS, START_NUMBER,FORBIDDEN_CHARACTERS
import os

def build_new_name(old_name,prefix,suffix, number):
    name, extension = os.path.splitext(old_name)
    sec_number = str(number).zfill(NUMBER_DIGITS)
    return (f'{prefix}{sec_number}{suffix}{extension}')


def search_files(path, prefix, suffix):
    files_list = []
    
    for number, name in enumerate(os.listdir(path), START_NUMBER):
        full_path = os.path.join(path,name)
        if os.path.isfile(full_path):
            new_name = build_new_name(name, prefix, suffix, number)
            files_list.append({'old_name': name, 'new_name': new_name})
    
    return files_list

    
def execute_rename(path, files_list):
    successful_renames = []
    
    for file in files_list:
        old_path = os.path.join(path,file['old_name'])
        new_path = os.path.join(path,file['new_name'])
        try:
            os.rename(old_path,new_path)
            successful_renames.append(file)
        except FileExistsError as e:
            print(f"Could not rename {file['old_name']}: {e}")
    
    return successful_renames       

def undo_rename(path, successful_renames):
    for file in successful_renames:
        target_path = os.path.join(path,file['old_name'])
        current_path = os.path.join(path,file['new_name'])
        try:
            os.rename(current_path,target_path)
        except FileExistsError as e:
            print(f"Could not rename {file['old_name']}: {e}")
            
def get_valid_folder():
    while True:
        folder= input('Enter a valid folder ')
        if not os.path.isdir(folder):
            print('That is not a valid folder')
        else:
            return folder

def get_valid_prefix_and_suffix(prompt):
    
    while True:
        names = input(prompt)
        for char in FORBIDDEN_CHARACTERS:
            if char in names:
                print('Do not enter an invalid character @\/<>*?:"')
            else:
                continue
        return names
    
            
    
def get_valid_text(prompt):
    while True:
        names = input(prompt)
        has_forbidden_char = False
        for char in FORBIDDEN_CHARACTERS:
            if char in names:
                has_forbidden_char = True
        if has_forbidden_char:
            print('Do not enter an invalid character @\\/<>*?:"')
        else:
            return names
