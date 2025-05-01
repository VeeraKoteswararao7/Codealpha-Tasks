import os
import shutil
import datetime

folder_path = input("Enter folder path: ")
backup_path = os.path.join(folder_path, "backup_" + datetime.datetime.now().strftime("%Y%m%d_%H%M%S"))

# Create a backup directory
os.makedirs(backup_path, exist_ok=True)

extensions = {
    'Images': ['.jpeg', '.jpg', '.png', '.gif', '.JPG'],
    'Documents': ['.doc', '.docx', '.pdf', '.txt', '.xls', '.xlsx', '.rtf', '.xlsm', '.ppt', '.pptx'],
    'Music': ['.mp3', '.wav'],
    'Videos': ['.mp4', '.avi', '.mkv', '.webm'],
    'Compressed': ['.zip', '.rar'],
    'Software': ['.exe'],
    'Adobe Preset': ['.prfpset'],
    'Icon Pack': ['.ico'],
    'RainMeter': ['.rmskin'],
    'NodeJs': ['.msi']
}

for filename in os.listdir(folder_path):
    for category, exts in extensions.items():
        for ext in exts:
            if filename.endswith(ext):
                source_path = os.path.join(folder_path, filename)
                destination_path = os.path.join(folder_path, category)

                # Create category folder if it doesn't exist
                if not os.path.exists(destination_path):
                    os.makedirs(destination_path)

                # Backup the file
                shutil.copy2(source_path, backup_path)
                print(f"Backed up {filename} to {backup_path}")

                # Check for file duplication
                destination_file_path = os.path.join(destination_path, filename)
                if os.path.exists(destination_file_path):
                    print(f"File {filename} already exists in {category}. Skipping move.")
                else:
                    # Move file to category folder
                    shutil.move(source_path, destination_path)
                    print(f"Moved {filename} to {category}")

                # Exit inner for loop if file has been moved or backed up
                break

# Indicate completion of the task
print("\n\nBackup and organization task completed.")

Enter folder path: C:\Users\veerakoteswararao7\Downloads


Backup and organization task completed.
