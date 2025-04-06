def modify_content(content):
    # Modify the content 
    # Convert it to uppercase
    return content.upper()

try:
    # Ask user for filename
    source_file = input("Enter the name of the file to read from: ")

    # Try to open and read the file
    with open(source_file, "r") as file:
        original_content = file.read()

    # Modify the content
    modified_content = modify_content(original_content)

    # Write the modified content to a new file
    output_file = "modified_" + source_file
    with open(output_file, "w") as file:
        file.write(modified_content)

    print(f"Modified content saved to '{output_file}'.")

except FileNotFoundError:
    print(" Error: File not found. Please check the filename and try again.")
except IOError:
    print(" Error: Unable to read or write to the file.")
