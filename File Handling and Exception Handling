def read_and_modify_file():
    try:
        # Ask user for the input filename
        input_filename = input("Enter the name of the file to read: ")

        # Try opening the file for reading
        with open(input_filename, 'r') as infile:
            content = infile.read()
        
        # Modify the content (example: make it uppercase)
        modified_content = content.upper()

        # Ask user for the output filename
        output_filename = input("Enter the name of the new file to write to: ")
        
        # Write modified content to new file
        with open(output_filename, 'w') as outfile:
            outfile.write(modified_content)
        
        print(f"File '{output_filename}' created successfully with modified content!")

    except FileNotFoundError:
        print("🚫 Error: File not found. Please check the filename and try again.")
    except IOError:
        print("🚫 Error: Unable to read or write the file. Check permissions or disk space.")
    except Exception as e:
        print(f"🚫 An unexpected error occurred: {e}")

# Run the function
read_and_modify_file()
