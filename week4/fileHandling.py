def read_and_modify_file():
    filename = input("Enter the name of the file to read: ")

    try:
        with open(filename, "r") as infile:
            content = infile.read()

        modified_content = content.upper()

        new_filename = "modified_" + filename

        with open(new_filename, "w") as outfile:
            outfile.write(modified_content)

        print(f"File modified successfully! Saved as '{new_filename}'")

    except FileNotFoundError:
        print("❌ Error: The file does not exist.")
    except PermissionError:
        print("❌ Error: You don’t have permission to read this file.")
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")


read_and_modify_file()
