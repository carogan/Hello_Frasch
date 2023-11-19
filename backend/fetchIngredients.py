import os
import json 

# Specify the directory path
directory_path = 'backend/Data'

# Get a list of all files in the directory
files = os.listdir(directory_path)

# Create a dictionary to store file names without the file extension
file_names_list = []

# Iterate through the files and store names without the extension
for file_name in files:
    # Get the file name without the extension
    name_without_extension, _ = os.path.splitext(file_name)
    
    # Store in the dictionary
    file_names_list.append(name_without_extension)

# Print the resulting dictionary
f = open("backend/ingredientsList.py", "a")
f.write("ingredients = " +str(file_names_list))

f.close()