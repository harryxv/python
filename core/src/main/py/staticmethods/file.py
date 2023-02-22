# Reading from file; write to file
# use open() function
fromFile = open("len.py", "r")
toFile = open("len_copy.txt", "w")
for line in fromFile:
    line = line.strip()
    print(line)
    toFile.write(line)
fromFile.close()
toFile.close()


