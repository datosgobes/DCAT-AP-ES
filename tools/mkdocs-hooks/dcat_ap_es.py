import os
import shutil

def on_post_build(config, **kwargs):
    """
    Post-build hook to copy PDF files from the source directory to the destination directory.

    This function is intended to be used as a MkDocs plugin hook. It copies all files and directories
    from the specified source directory to the specified destination directory within the site directory.

    Args:
        config (dict): The MkDocs configuration dictionary.
        **kwargs: Additional keyword arguments.

    Raises:
        FileNotFoundError: If the source directory does not exist.
        PermissionError: If there are permission issues accessing the directories.
    """
    source_dir = config['extra']['mkdocs_hooks']['pdf_source']
    destination_dir = os.path.join(config['site_dir'], config['extra']['mkdocs_hooks']['pdf_dest'])

    # Ensure the destination directory exists
    os.makedirs(destination_dir, exist_ok=True)

    # Copy all files and directories from source to destination
    for item in os.listdir(source_dir):
        s = os.path.join(source_dir, item)
        d = os.path.join(destination_dir, item)
        if os.path.isdir(s):
            shutil.copytree(s, d, dirs_exist_ok=True)
        else:
            shutil.copy2(s, d)