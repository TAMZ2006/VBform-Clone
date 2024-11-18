import os
import glob

# Locate the base .resx file
resx_files = glob.glob("*.resx")
if resx_files:
    base_resx_file = resx_files[0]
    base_name = os.path.splitext(base_resx_file)[0]
else:
    raise FileNotFoundError("No .resx file found in the current directory.")

# Get the new file name from the user
new_name = input("Enter the new file name (e.g., Stock_low): ")

# File names to be processed
folder_path = "./"  # assuming the files are in the current directory
files = [
    f"{base_name}.vb",
    f"{base_name}.Designer.vb",
    f"{base_name}.resx"
]

# Define the mapping for renaming the files
renamed_files = {
    f"{base_name}.vb": f"{new_name}.vb",
    f"{base_name}.Designer.vb": f"{new_name}.Designer.vb",
    f"{base_name}.resx": f"{new_name}.resx"
}

# Rename the files with existence check
for old_name, new_file_name in renamed_files.items():
    old_path = os.path.join(folder_path, old_name)
    new_path = os.path.join(folder_path, new_file_name)
    if os.path.exists(old_path):
        os.rename(old_path, new_path)
    else:
        print(f"Warning: {old_path} does not exist and cannot be renamed.")

# Update content in .Designer.vb and .vb files if they exist
if os.path.exists(renamed_files[f"{base_name}.Designer.vb"]):
    with open(renamed_files[f"{base_name}.Designer.vb"], "r") as file:
        content = file.read()
    
    # Replace "Partial Class {base_name}" with "Partial Class {new_name}"
    content = content.replace(f"Partial Class {base_name}", f"Partial Class {new_name}")
    
    with open(renamed_files[f"{base_name}.Designer.vb"], "w") as file:
        file.write(content)
else:
    print(f"Warning: {renamed_files[f'{base_name}.Designer.vb']} does not exist and cannot be updated.")

if os.path.exists(renamed_files[f"{base_name}.vb"]):
    with open(renamed_files[f"{base_name}.vb"], "r") as file:
        content = file.read()
    
    # Replace "Public Class {base_name}" with "Public Class {new_name}"
    content = content.replace(f"Public Class {base_name}", f"Public Class {new_name}")
    
    # Replace "Private Sub {base_name}_Load(sender As Object, e As EventArgs) Handles MyBase.Load"
    # with "Private Sub {new_name}_Load(sender As Object, e As EventArgs) Handles MyBase.Load"
    content = content.replace(
        f"Private Sub {base_name}_Load(sender As Object, e As EventArgs) Handles MyBase.Load",
        f"Private Sub {new_name}_Load(sender As Object, e As EventArgs) Handles MyBase.Load"
    )
    
    with open(renamed_files[f"{base_name}.vb"], "w") as file:
        file.write(content)
else:
    print(f"Warning: {renamed_files[f'{base_name}.vb']} does not exist and cannot be updated.")

# Update the .vbproj file
vbproj_files = glob.glob("*.vbproj")
if vbproj_files:
    vbproj_file = vbproj_files[0]
else:
    raise FileNotFoundError("No .vbproj file found in the current directory.")

# Read the .vbproj file and inject the new Compile and EmbeddedResource elements
with open(vbproj_file, "r") as file:
    vbproj_content = file.readlines()

new_compile_entries = f"\n\t<Compile Include=\"{new_name}.Designer.vb\">\n\t\t<DependentUpon>{new_name}.vb</DependentUpon>\n\t</Compile>\n\t<Compile Include=\"{new_name}.vb\">\n\t\t<SubType>Form</SubType>\n\t</Compile>\n"
new_embedded_resource_entry = f"\n\t<EmbeddedResource Include=\"{new_name}.resx\">\n\t\t<DependentUpon>{new_name}.vb</DependentUpon>\n\t</EmbeddedResource>\n"

# Locate where to insert the new Compile entries
for index, line in enumerate(vbproj_content):
    if f"<Compile Include=\"{base_name}.vb\">" in line:
        vbproj_content.insert(index, new_compile_entries)
        break

# Locate where to insert the new EmbeddedResource entry
for index, line in enumerate(vbproj_content):
    if f"<EmbeddedResource Include=\"{base_name}.resx\">" in line:
        vbproj_content.insert(index, new_embedded_resource_entry)
        break

# Write the updated content back to the .vbproj file
with open(vbproj_file, "w") as file:
    file.writelines(vbproj_content)

print("Files and .vbproj file have been updated successfully.")

