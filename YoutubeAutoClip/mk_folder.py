import os

def create_folder_if_not_exists(id):
    path = './output/'+id
    if not os.path.exists(path):
        os.makedirs(path)
        print(f"Folder '{path}' created.")
    else:
        print(f"Folder '{path}' already exists.")