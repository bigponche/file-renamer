from core import search_files,get_valid_folder,get_valid_text,execute_rename,undo_rename,show_dry_run

def get_confirmation(prompt):
    while True:
        confirmation = input(prompt)
        if confirmation.lower().strip() == 'y':
            return True
        elif confirmation.lower().strip() == 'n':
            return False
        else:
            print('choose a valid option')
            