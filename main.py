"""
Main script for the AI-powered screenshot organizer.
This script uses multiple AI agents to:
1. Find and read the newest screenshot
2. Generate a descriptive filename
3. Categorize the screenshot
4. Move the file to its appropriate category
"""

import os

from pydantic import BaseModel
from pydantic_ai import Agent, BinaryContent, Tool

from helpers import SCREENSHOTS_DIRECTORY, rename_and_move_screenshot
from helpers import list_categories, get_newest_screenshot, create_directory

# Get the most recent screenshot file
newest_screenshot = get_newest_screenshot()

# Read the screenshot file into binary data for AI processing
with open(os.path.join(SCREENSHOTS_DIRECTORY, newest_screenshot), "rb") as file:
    data = file.read()

# Create an AI agent for generating descriptive filenames
# This agent analyzes the screenshot and suggests an appropriate name
rename_file_agent = Agent(
    "openai:gpt-4.1-mini-2025-04-14",
    system_prompt="Come up with a descriptive filename for the following screenshot."
)

# Process the screenshot and get the suggested filename
result = rename_file_agent.run_sync([BinaryContent(data=data, media_type="image/png")])
print(result.output)
filename = result.output

# Define a data model for category responses
class Category(BaseModel):
    category: str

# Create an AI agent for categorizing screenshots
# This agent decides whether to use an existing category or create a new one
category_agent = Agent(
    "openai:gpt-4.1-mini-2025-04-14",
    system_prompt="""You will get a list of categories and then you'll get a filename for a screenshot. 
        Decide if the screenshot belongs in an existing category or if a new category should be created for that screenshot. 
        And then return the category.""",
    output_type=Category
)

# Get category suggestion based on existing categories and the new filename
result = category_agent.run_sync(f"""
    Categories: {list_categories()}
    Filename: {filename}
""")

category = result.output.category

# Create an AI agent for file operations
# This agent handles the actual file movement and organization
move_file_agent = Agent(
    "openai:gpt-4.1-mini-2025-04-14",
    system_prompt="You'll get a filename and a category. Use the tools to first create a category and then move the file to that category folder.",
    tools=[Tool(create_directory, takes_ctx=False), Tool(rename_and_move_screenshot, takes_ctx=False)]
)

# Execute the file organization with the chosen category and filename
move_file_agent.run_sync(
    f"Old filename: {newest_screenshot}\n" \
    f"New filename: {category}/{filename}\n" \
    f"Category: {category}"
)