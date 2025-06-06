# AI Screenshot Organizer

A Python-based tool for organizing screenshots into categories using AI assistance. This tool helps you manage your screenshots by providing functionality to move, rename, and categorize them efficiently.

## Features

- Automatically detect the newest screenshot in the designated directory
- Create and manage screenshot categories
- Move and rename screenshots
- Support for JPG image format

## Setup

1. Ensure you have Python 3.13 or higher installed
2. Install the required dependencies:
```bash
pip install -r requirements.txt
```
3. Set up your OpenAI API key:
```bash
export OPENAI_API_KEY='your-api-key-here'
```
   - You can get your API key from the [OpenAI dashboard](https://platform.openai.com/api-keys)
   - For persistent access, add the export command to your shell's config file (e.g., `~/.zshrc` or `~/.bashrc`)

## Project Structure

- `screenshots/` - Main directory where screenshots are stored and organized
- `helpers.py` - Core utility functions for file operations
- `main.py` - Main application logic

## Usage

The tool provides several key functions:

### Get Newest Screenshot
```python
from helpers import get_newest_screenshot

newest_file = get_newest_screenshot()
```

### List Categories
```python
from helpers import list_categories

categories = list_categories()
print(categories)  # Prints available categories
```

### Create New Category
```python
from helpers import create_directory

create_directory("my_category")  # Creates a new category folder
```

### Move and Rename Screenshots
```python
from helpers import rename_and_move_screenshot

rename_and_move_screenshot("old_name.jpg", "new_name.jpg")
```

## Directory Structure

```
ai-screenshot-organizer/
├── screenshots/
│   ├── category1/
│   ├── category2/
│   └── ...
├── helpers.py
├── main.py
└── README.md
```

## Dependencies

- pydantic >= 2.11.5
- pydantic-ai >= 0.2.15

## Note

Make sure the `screenshots` directory exists in your project root before running the application. Screenshots should be in JPG format.

## Acknowledgments

Special thanks to Anthony from [PrettyPrinted](https://youtu.be/qfPeXwYS1EA?si=OKvpagAs1VDVnYXx) for the excellent tutorial that helped inspire this project. His clear explanations and practical examples were invaluable in developing this tool.
