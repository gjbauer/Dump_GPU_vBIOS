#!/usr/bin/python3

# Open the file in read mode
file = open("grub", "r")

# Read each line one by one
for line in file:
	if "GRUB_CMDLINE_LINUX_DEFAULT" in line:  # .strip() to remove newline characters
		print(line.strip())
		break

for line in file:
	if "GRUB_CMDLINE_LINUX" in line:  # .strip() to remove newline characters
		print(line.strip())
		break

# Close the file
file.close()
