from core import search_files,get_valid_folder,get_valid_text,execute_rename,undo_rename,show_dry_run,get_confirmation

def main():
    folder = get_valid_folder()
    prefix = get_valid_text('Enter a valid prefix ')
    suffix = get_valid_text('Enter a valid suffix ')
    search = search_files(folder,prefix,suffix)
    show_dry_run(search)
    confirm = get_confirmation('Confirm the changes Y/N ')
    if confirm:
        execute = execute_rename(folder,search)
        confirm = get_confirmation('Undo the changes Y/N ')
        if confirm:
            undo_rename(folder,execute)

if __name__ == "__main__":
    main()