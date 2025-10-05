# File Handling in Python 


file = open("filename", "mode")


# Example 1 – Open a file for reading
f = open("demo.txt", "r")
print(f.read())
f.close()

# Example 2 – Open a file for writing
f = open("demo.txt", "w")
f.write("Hello Python!")
f.close()

# Example 3 – Open a file for appending
f = open("demo.txt", "a")
f.write("\nAppending new text.")
f.close()

# Example 4 – Using with open() (auto close)
with open("demo.txt", "r") as f:
    print(f.read())

# Example 5 – Create a file if it doesn’t exist
f = open("newfile.txt", "x")
f.write("This is a newly created file.")
f.close()

# Reading Files

# You can read text files using .read(), .readline(), or .readlines().

# Examples:
# Example 1 – Read entire file
with open("demo.txt", "r") as f:
    content = f.read()
    print(content)

# Example 2 – Read first 10 characters
with open("demo.txt", "r") as f:
    print(f.read(10))

# Example 3 – Read line by line
with open("demo.txt", "r") as f:
    print(f.readline())  # reads first line

# Example 4 – Read all lines into a list
with open("demo.txt", "r") as f:
    lines = f.readlines()
    print(lines)

# Example 5 – Loop through file lines
with open("demo.txt", "r") as f:
    for line in f:
        print(line.strip())

#  3. Writing Files


# Example 1 – Write new content
with open("write.txt", "w") as f:
    f.write("Writing new content to file.")

# Example 2 – Overwrite content
with open("write.txt", "w") as f:
    f.write("This will replace existing text.")

# Example 3 – Append to file
with open("write.txt", "a") as f:
    f.write("\nThis line is appended.")

# Example 4 – Write multiple lines
lines = ["Python\n", "File Handling\n", "Examples\n"]
with open("multi.txt", "w") as f:
    f.writelines(lines)

# Example 5 – Write user input
text = input("Enter text to save: ")
with open("input.txt", "w") as f:
    f.write(text)

# 4. Working with Binary Files

# Binary files store data like images, videos, or PDFs.

# Examples:
# Example 1 – Read binary data
with open("image.jpg", "rb") as f:
    data = f.read()
    print(len(data))

# Example 2 – Copy binary file
with open("image.jpg", "rb") as src:
    with open("copy.jpg", "wb") as dst:
        dst.write(src.read())

# Example 3 – Write binary data
data = b"BinaryDataExample"
with open("binary.bin", "wb") as f:
    f.write(data)

# Example 4 – Append binary data
with open("binary.bin", "ab") as f:
    f.write(b"MoreBinaryData")

# Example 5 – Read binary in chunks
with open("largefile.bin", "rb") as f:
    chunk = f.read(1024)
    while chunk:
        print(len(chunk))
        chunk = f.read(1024)

# 5. Using with Statement (Best Practice)

# Using with open() ensures automatic file closing.

# Examples:
# Example 1
with open("sample.txt", "w") as f:
    f.write("Safe write with with statement.")

# Example 2
with open("sample.txt", "r") as f:
    print(f.read())

# Example 3
with open("sample.txt", "a") as f:
    f.write("\nAppended safely.")

# Example 4
with open("sample.txt", "r") as f:
    for line in f:
        print(line.strip())

# Example 5
with open("numbers.txt", "w") as f:
    for i in range(5):
        f.write(f"Number {i}\n")

# 6. Deleting Files

# Use the os module to delete files.

# Examples:
# Example 1 – Basic file delete
import os
os.remove("demo.txt")

# Example 2 – Check before deleting
import os
if os.path.exists("demo.txt"):
    os.remove("demo.txt")
else:
    print("File not found.")

# Example 3 – Delete inside a directory
import os
os.remove("folder/temp.txt")

# Example 4 – Delete multiple files
import os
for f in ["a.txt", "b.txt", "c.txt"]:
    if os.path.exists(f):
        os.remove(f)

# Example 5 – Delete all .log files
import os, glob
for file in glob.glob("*.log"):
    os.remove(file)

# 7. Exception Handling in File Operations

# Always handle potential errors like missing files.

# Examples:
# Example 1
try:
    f = open("missing.txt", "r")
except FileNotFoundError:
    print("File not found!")

# Example 2
try:
    with open("data.txt", "r") as f:
        print(f.read())
except Exception as e:
    print("Error:", e)

# Example 3
try:
    with open("readonly.txt", "w") as f:
        f.write("Can't write here!")
except PermissionError:
    print("No permission!")

# Example 4
try:
    f = open("demo.txt", "x")
except FileExistsError:
    print("File already exists!")

# Example 5
try:
    with open("numbers.txt") as f:
        for line in f:
            print(int(line))
except ValueError:
    print("Not a valid number in file.")

#  8. Handling CSV Files

# Python has a built-in csv module for handling CSV files.

#  Examples:
# Example 1 – Write CSV
import csv
with open("data.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Name", "Age"])
    writer.writerow(["Alice", 25])

# Example 2 – Read CSV
import csv
with open("data.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

# Example 3 – Write multiple rows
import csv
data = [["Name", "City"], ["Bob", "Delhi"], ["Eve", "London"]]
with open("people.csv", "w", newline="") as f:
    csv.writer(f).writerows(data)

# Example 4 – Read with DictReader
import csv
with open("people.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row["Name"], row["City"])

# Example 5 – Append to CSV
import csv
with open("data.csv", "a", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["John", 30])

#  9. Handling JSON Files

# The json module helps store and read structured data.

#  Examples:
# Example 1 – Write JSON
import json
data = {"name": "Alice", "age": 25}
with open("data.json", "w") as f:
    json.dump(data, f)

# Example 2 – Read JSON
import json
with open("data.json", "r") as f:
    data = json.load(f)
    print(data)

# Example 3 – Pretty-print JSON
import json
data = {"students": [{"name": "A"}, {"name": "B"}]}
print(json.dumps(data, indent=4))

# Example 4 – Append new data
import json
with open("data.json", "r") as f:
    data = json.load(f)
data["city"] = "New York"
with open("data.json", "w") as f:
    json.dump(data, f, indent=4)

# Example 5 – Convert Python object to JSON string
import json
person = {"name": "Charlie", "age": 28}
json_string = json.dumps(person)
print(json_string)

