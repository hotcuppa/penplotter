import os
import sys

def edit_text_in_file(file_name, delimiter='|'):
    # Get the path of the replacements file in the same folder as the script
    script_dir = os.path.dirname(os.path.realpath(__file__))
    replacements_file = os.path.join(script_dir, 'replacements.txt')

    # Open the replacements file
    with open(replacements_file, 'r') as replacements:
        # Read the content of the replacements file
        lines = replacements.readlines()

        # Initialize dictionaries to store old and new text
        old_new_pairs = {}

        # Iterate through each line in the replacements file
        for line in lines:
            # Split the line into old and new text using the specified delimiter
            parts = line.strip().split(delimiter)
            if len(parts) == 2:
                old_text, new_text = parts
                # Replace {newline} with an actual newline character
                new_text = new_text.replace('{newline}', '\n')
            elif len(parts) == 1:
                # If only one part is present, set new_text as empty
                old_text, new_text = parts[0], ''
            else:
                # Invalid line format
                print(f"Invalid line format in replacements file: {line.strip()}")
                continue

            # Store the old and new text in the dictionary
            old_new_pairs[old_text] = new_text

    # Open the file in read mode
    with open(file_name, 'r') as file:
        # Read the content
        content = file.read()

    # Perform the text replacements
    for old_text, new_text in old_new_pairs.items():
        content = content.replace(old_text, new_text)

    # Open the file in write mode to overwrite the content
    with open(file_name, 'w') as file:
        # Write the modified content back to the file
        file.write(content)

# Example usage
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python edit_file.py <file_name>")
        sys.exit(1)

    file_name = sys.argv[1]
    edit_text_in_file(file_name)
