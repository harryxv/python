# Reading from file; write to file
# use open() function
src_file = open("len.py", "r")
target_file = open("len_copy.txt", "w")
for line in src_file:
    line = line.strip()
    print(line)
    target_file.write(line)
src_file.close()
target_file.close()
