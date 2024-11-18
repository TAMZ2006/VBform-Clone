# VBform-Clone

# Clone Form Tool

A simple tool to clone and rename forms for your .NET projects. **Note**: This tool is designed for **basic projects** and may not handle advanced use cases or complex project structures.

---

## Features
- Quickly duplicate existing forms.
- Automatically rename and update associated files.
- Seamlessly integrate the cloned form into your project.

---

## How to Use

### Step 1: Prepare Your Folder
1. Create a new folder for the cloned form.
2. Copy the following files from the form you want to clone into this folder:
   - `.vb` (Main code file)
   - `.designer.vb` (Designer code file)
   - `.resx` (Resource file)

---

### Step 2: Add the Main Project File
1. Copy the main `.vbproj` file of your project into the same folder.
2. Ensure all required files are in place.

---

### Step 3: Run the Tool
1. Launch the Clone Form Tool.
2. Follow the on-screen prompts:
   - Enter the **new name** for the cloned form.
   - Verify that the tool has renamed all necessary files and references.

---

### Step 4: Integrate the Cloned Form
1. Move all the generated files back into your main solution folder.
2. When prompted to replace the `.vbproj` file, click **OK**.
3. Open your project in Visual Studio and ensure the cloned form appears correctly.

---

### Step 5: Resolve Potential Namespace Conflicts
1. Open the cloned `.vb` file in your project.
2. Check for any `Public` classes or other elements in the original form that might cause a **namespace conflict**.
   - If found, update the class declarations or remove unnecessary `Public` modifiers.
3. Make sure the class name matches the new form name to avoid build errors.

---

### Step 6: Test the Project
1. Build and run the project to verify that the cloned form works as expected.
2. Make any adjustments to the cloned form if needed.

---

## Notes and Limitations
- **Basic Projects Only**: This tool is rudimentary and intended for basic projects. It may not handle advanced scenarios such as:
  - Complex namespaces.
  - Multi-project solutions.
- **Namespace Conflicts**: You must manually resolve potential namespace conflicts caused by `Public` classes or other similar elements.
- Always back up your project before making significant changes.

---

Feel free to contribute or report any issues with this tool!
