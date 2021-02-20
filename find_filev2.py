from pathlib import Path
import os

# Variables containing windows path object, string concatenated.
documents = Path.home() / Path('Documents')
downloads = Path.home() / Path('Downloads')

# Asks us which directory we want to use, store in path variable.
choose_directory = input("Directories: documents or downloads? ").lower()

"""
list_path takes the arguments documents or downloads. If 
user chooses documents they will get the option to append 
text to the chosen file after the files in the Documents directory are listed.

If user chooses downloads they will get a listing of the downloads directory
and get asked if they would like to delete a file. 
"""


def list_path(directory):
    if directory == "documents":
        print(f"Documents is located at: {documents}\n")
        for file in documents.glob('*'):
            print(file)
        edit_file = input("\nEdit file? (Y/N)").upper()
        if edit_file == 'Y':
            file_edit = input("\nWhich file? ")
            answer = documents / file_edit
            with open(answer, 'a') as file:
                file.write("\n")
                file.write(input("\nEnter text: "))
        elif edit_file == 'N':
            print("\nFinished...")

    elif directory == "downloads":
        print(f"Downloads is located at: {downloads}\n")
        for file in downloads.glob('*'):
            print(file)
        delete_file = input("\nDelete a file? (Y/N)").upper()
        if delete_file == "Y":
            file_delete = input("\nDelete: ")
            answer = downloads / Path(file_delete)
            print(f"\nRemoving: {file_delete}")
            os.remove(answer)
        elif delete_file == "N":
            print("\nFiles kept, good day.")


# Call our function list_path with directory stored in choose_directory
list_path(choose_directory)
