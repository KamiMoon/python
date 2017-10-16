filename = 'analyze_text.txt'

try:
    with open(filename) as file_object:
        contents = file_object.read()
except FileNotFoundError:
    print("File doesn't exist")
else:
    print(contents.lower().count('the'))