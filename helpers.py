"""
Helper functions for managing screenshot organization.
This module provides utility functions for managing screenshots, including
finding the newest screenshot, listing categories, and moving files.
"""

import os
import shutil

# Base directory where all screenshots and category folders are stored
SCREENSHOTS_DIRECTORY = "screenshots"

def get_newest_screenshot() -> str:
    """
    Find the most recently created JPG file in the screenshots directory.
    
    Returns:
        str: The filename of the newest screenshot, or None if no screenshots are found.
        
    Note:
        Only considers files with .jpg extension
        Uses file creation time to determine the newest file
    """
    files = [f for f in os.listdir(SCREENSHOTS_DIRECTORY) if f.endswith('.jpg')]
    if not files:
        return None
    newest_file = max(files, key=lambda f: os.path.getctime(os.path.join(SCREENSHOTS_DIRECTORY, f)))
    return newest_file

def list_categories() -> str:
    """
    Get a string listing of all category directories in the screenshots folder.
    
    Returns:
        str: A newline-separated string of category names.
        
    Note:
        Only includes directories, not files
        Each category name is followed by a newline character
    """
    categories = ""
    for category in os.listdir(SCREENSHOTS_DIRECTORY):
        category_path = os.path.join(SCREENSHOTS_DIRECTORY, category)
        if os.path.isdir(category_path):
            categories += f"{category}\n"
    return categories

def create_directory(directory_name: str) -> None:
    """
    Create a new category directory within the screenshots folder.
    
    Args:
        directory_name (str): Name of the directory to create
        
    Note:
        Creates the directory only if it doesn't already exist
        Creates the full path if parent directories don't exist
    """
    new_directory_path = os.path.join(SCREENSHOTS_DIRECTORY, directory_name)
    if not os.path.exists(new_directory_path):
        os.makedirs(new_directory_path)

def rename_and_move_screenshot(filename: str, new_name: str) -> None:
    """
    Rename and/or move a screenshot file to a new location.
    
    Args:
        filename (str): Current name of the screenshot file
        new_name (str): New name/path for the screenshot file
        
    Note:
        Can move files between directories
        Will overwrite destination file if it exists
        Uses shutil.move which handles cross-device moves
    """
    source_path = os.path.join(SCREENSHOTS_DIRECTORY, filename)
    destination_path = os.path.join(SCREENSHOTS_DIRECTORY, new_name)
    shutil.move(source_path, destination_path)