def read_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            return content
    except FileNotFoundError:
        return "Error: File not found"
    except Exception as e:
        return f"Unexpected error: {e}"