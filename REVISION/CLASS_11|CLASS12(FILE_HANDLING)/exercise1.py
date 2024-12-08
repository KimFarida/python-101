"""
Create a function called 'safe_read' that:
1. Takes a filename as input
2. Returns the file contents if file exists
3. Returns None if file doesn't exist
4. Uses proper exception handling
"""
def safe_read(filename):
    # Implement this function
    try:
        with open(filename, 'r') as file:
            return file.read()
    except FileExistsError:
        print("Not Exist")
        return None