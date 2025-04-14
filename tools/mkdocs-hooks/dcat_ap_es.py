import os
import shutil

def on_post_build(config, **kwargs):
    """
    Post-build hook to copy PDF and SHACL files from source directories to destination directories.

    This function is intended to be used as a MkDocs plugin hook. It copies:
    1. PDF files from the specified PDF source directory to the PDF destination directory
    2. SHACL files from the specified SHACL source directory to the SHACL destination directory

    The function preserves the directory structure when copying files, ensuring that
    subdirectories (like 'hvd') are properly maintained in the destination.

    Args:
        config (dict): The MkDocs configuration dictionary.
        **kwargs: Additional keyword arguments.

    Raises:
        FileNotFoundError: If the source directory does not exist.
        PermissionError: If there are permission issues accessing the directories.
    """
    # Get application profile version
    app_version = config['extra']['application_profile_version']
    
    # Copy PDF files
    pdf_source_dir = config['extra']['mkdocs_hooks']['pdf_source']
    pdf_dest_dir = os.path.join(config['site_dir'], config['extra']['mkdocs_hooks']['pdf_dest'])
    
    # Ensure the PDF destination directory exists
    os.makedirs(pdf_dest_dir, exist_ok=True)
    
    # Copy all PDF files and directories from source to destination
    for item in os.listdir(pdf_source_dir):
        s = os.path.join(pdf_source_dir, item)
        d = os.path.join(pdf_dest_dir, item)
        if os.path.isdir(s):
            shutil.copytree(s, d, dirs_exist_ok=True)
        else:
            shutil.copy2(s, d)
    
    # Copy SHACL files
    shacl_source_dir = os.path.join(config['extra']['mkdocs_hooks']['shacl_source'].format(
        application_profile_version=app_version))
    shacl_dest_dir = os.path.join(config['site_dir'], 
        config['extra']['mkdocs_hooks']['shacl_dest'].format(
            application_profile_version=app_version))

    # Ensure the destination directory exists
    os.makedirs(shacl_dest_dir, exist_ok=True)

    # Walk through the source directory
    for root, dirs, files in os.walk(shacl_source_dir):
        # Calculate the relative path but skip the version number segment
        # This changes from "shacl/1.0.0/hvd/file.ttl" to "shacl/hvd/file.ttl"
        rel_path = os.path.relpath(root, shacl_source_dir)
        
        # Create the corresponding directory in the destination
        dest_path = os.path.join(shacl_dest_dir, rel_path) if rel_path != '.' else shacl_dest_dir
        os.makedirs(dest_path, exist_ok=True)
        
        # Copy all files in the current directory
        for file in files:
            src_file = os.path.join(root, file)
            dst_file = os.path.join(dest_path, file)
            shutil.copy2(src_file, dst_file)
    
    print(f"✓ Copied PDF files to {pdf_dest_dir}")
    print(f"✓ Copied SHACL files to {shacl_dest_dir}")