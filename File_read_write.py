import re
import os

def search_replace_in_file(filepath, search_pattern, replace_pattern):
    """
    Reads a file, performs a regex search and replace, and overwrites the file.
    """
    try:
        # Read the content from the file
        with open(filepath, 'r') as file:
            content = file.read()
        
        # Perform the search and replace using re.sub
        # re.sub(pattern, repl, string, count=0, flags=0)
        new_content, num_replacements = re.subn(search_pattern, replace_pattern, content)
        
        # Write the modified content back to the file
        with open(filepath, 'w') as file:
            file.write(new_content)
            
        print(f"Successfully replaced {num_replacements} instance(s) in {filepath}")

    except FileNotFoundError:
        print(f"Error: The file '{filepath}' was not found.")
    except PermissionError:
        print(f"Error: You do not have permission to read/write to '{filepath}'.")
    except re.error as e:
        print(f"Error: Invalid regular expression: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# --- Main execution ---
if __name__ == "__main__":
    # Get user input
    filepath = input("Enter the path to your file: ")
    search_pattern = input("Enter the regex pattern to search for: ")
    replace_pattern = input("Enter the replacement string: ")

    # Check if the file exists before proceeding
    if not os.path.exists(filepath):
        print(f"The file '{filepath}' does not exist. Please check the path.")
    else:
        search_replace_in_file(filepath, search_pattern, replace_pattern)