from requirements import NUMBER_DIGITS, START_NUMBER
import os

def build_new_name(old_name,prefix,suffix, number):
    name, extension = os.path.splitext(old_name)
    sec_number = str(number).zfill(NUMBER_DIGITS)
    return (f'{prefix}{sec_number}{suffix}{extension}')

def search_files(path, old_name):
    route = os.path.join('EJERCICIOS,foto')
    search = os.listdir(route)
    file = os.path.isfile(search)
    for i in enumerate(search,START_NUMBER)
        if file ==os.path.isfile(search)
        file = os.path.isfile(search)
