from pathlib import Path

# -- Constant with the new of the file to open
FILENAME = "U5.txt"

# -- Open and read the file
file_contents = Path(FILENAME).read_text()

# -- Print the contents on the console
index_start = file_contents.find('\n')
file_contents = file_contents[index_start + 1:]
file_contents.replace("\n", "")

print ("Body of the U5.txt file:\n",file_contents)