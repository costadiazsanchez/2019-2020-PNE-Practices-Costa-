from pathlib import Path

# -- Constant with the new of the file to open
FILENAME = "ADA.txt"

# -- Open and read the file
file_contents = Path(FILENAME).read_text()

# -- Print the contents on the console
index_start = file_contents.split('\n')
index_start = index_start [5:]    ## 5 because it is the number of lines until the beginning of the body.
gen = ''
for i in index_start:
    gen = gen + i

print ("The total number of bases is: ", len(gen))