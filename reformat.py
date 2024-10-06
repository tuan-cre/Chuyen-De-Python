import os

# Path to the main folder that contains all Chuong folders
main_directory = "D:\Chuyen-De-Python"
course_code = "DTH225757"

# Loop through each subfolder in the main directory
for chapter_folder in os.listdir(main_directory):
    chapter_path = os.path.join(main_directory, chapter_folder)
    
    # Check if it's a folder that starts with 'Chuong'
    if os.path.isdir(chapter_path) and chapter_folder.startswith("Chuong"):
        # Extract the chapter number, format it with leading zero, and keep the space
        chapter_number = chapter_folder.split(" ")[1].zfill(2)  # Extract and format the number with leading zero
        chapter = f"Chuong{chapter_number}"  # No space between 'Chuong' and the number
        
        # Loop through each file in the chapter folder
        for filename in os.listdir(chapter_path):
            # Check if the file follows the pattern "Bai X.py"
            if filename.startswith("Bai") and filename.endswith(".py"):
                # Extract the Bai number from the filename
                bai_number = filename.split(" ")[1].split(".")[0]
                # Format the Bai number with leading zeros
                bai_number = bai_number.zfill(2)
                
                # Create the new filename with the specified format
                new_filename = f"{course_code}.{chapter}.Bai{bai_number}.py"
                
                # Get full paths
                old_path = os.path.join(chapter_path, filename)
                new_path = os.path.join(chapter_path, new_filename)
                
                # Rename the file
                os.rename(old_path, new_path)
                print(f"Renamed '{filename}' in '{chapter_folder}' to '{new_filename}'")

print("All files in all Chuong folders have been renamed.")
