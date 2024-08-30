# Open the file in read mode
file_path = 'version'
try:
    with open(file_path, 'r') as file:
        # Read the content of the file
        file_content = file.read()
        # Print the content
        print("File Content:\n", file_content)
        # Read the first line of the file
        open(file_path) as f
        f: first_line=f.readline()
        # print the first line
        print("Latest version in first line:\n",first_line)

except FileNotFoundError:
    print(f"File '{file_path}' not found.")
except Exception as e:
    print(f"An error occurred: {e}")

