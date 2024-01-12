import os
import shutil

def create_folders_for_files(folder_path):
    # Get the list of Python files in the given folder
    python_files = [f for f in os.listdir(folder_path) if f.endswith('.py')]

    # Create a folder for each Python file
    for python_file in python_files:
        # Remove the ".py" extension
        file_name = os.path.splitext(python_file)[0]
        
        # Create a folder with the file name
        folder_name = os.path.join(folder_path, file_name)
        os.makedirs(folder_name, exist_ok=True)

        # Move the Python file into the created folder
        file_path = os.path.join(folder_path, python_file)
        shutil.move(file_path, os.path.join(folder_name, python_file))

if __name__ == "__main__":
    folder_path = "."

