#!/usr/bin/python3

# Open the file in read mode
file = open("grub", "r")

# Read each line one by one
for line in file:
    print(line.strip())  # .strip() to remove newline characters

# Close the file
file.close()
