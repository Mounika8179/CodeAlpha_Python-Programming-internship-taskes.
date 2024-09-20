import os
import shutil

def organize_files(directory):
    """Organize files in the specified directory into subdirectories by file type."""
    # Define the file type categories and their corresponding extensions
    file_types = {
        'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
        'Documents': ['.pdf', '.docx', '.txt', '.xlsx', '.pptx'],
        'Videos': ['.mp4', '.avi', '.mov', '.mkv'],
        'Music': ['.mp3', '.wav', '.aac'],
        'Archives': ['.zip', '.tar', '.gz']
    }
    
    # Create the subdirectories if they don't exist
    for folder in file_types.keys():
        folder_path = os.path.join(directory, folder)
        os.makedirs(folder_path, exist_ok=True)
    
    # Iterate through files in the specified directory
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)

        # Skip directories
        if os.path.isdir(file_path):
            continue
        
        # Get the file extension
        _, ext = os.path.splitext(filename)

        # Move the file to the corresponding subdirectory
        for folder, extensions in file_types.items():
            if ext.lower() in extensions:
                shutil.move(file_path, os.path.join(directory, folder, filename))
                print(f'Moved: {filename} to {folder}/')
                break
        else:
            print(f'No category found for: {filename}')

if __name__ == '__main__':
    target_directory = input("Enter the directory path to organize files: ")
    organize_files(target_directory)
    print("File organization complete!")
