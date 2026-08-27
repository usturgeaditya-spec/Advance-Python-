# Create input.txt with sample data
with open("input.txt", "w") as file:
    file.write("Hello Python\n")
    file.write("File handling is easy\n")
    file.write("This is the third line\n")
    file.write("This is the fourth line\n")

with open("input.txt", "r") as file:
    lines = file.readlines()

line_count = len(lines)

first_two_lines = lines[:2]

with open("output.txt", "w") as file:
    file.writelines(first_two_lines)

# Display the results
print("Total number of lines:", line_count)
print("First two lines:")
print("".join(first_two_lines))
print("First two lines have been written to output.txt")