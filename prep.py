#!/usr/bin/python3

# Open the file in read mode
file = open("/etc/default/grub", "r+")

# Read each line one by one
nf = list(line for line in file)

for l in nf:
	if "GRUB_CMDLINE_LINUX_DEFAULT" in l:  # Find the line we are looking for
		i = nf.index(l)
		s = "GRUB_CMDLINE_LINUX_DEFAULT=\"intel_iommu=on\" text"	# Replace it with our desired settings
		print(s)
		nf[i] = s

for l in nf:
	if "GRUB_CMDLINE_LINUX_DEFAULT" in l:  # .strip() to remove newline characters
		print(l.strip())


# Close the file
file.close()
