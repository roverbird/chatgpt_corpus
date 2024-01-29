import sys
import re

# Check that both input and output filenames, as well as min and max frequencies, were provided
if len(sys.argv) != 5:
    print('Usage: python program_name.py input_file_name output_file_name min_frequency max_frequency')
    sys.exit()

# Get the filenames and frequency values from the command-line arguments
input_file_name = sys.argv[1]
output_file_name = sys.argv[2]
min_frequency = int(sys.argv[3])
max_frequency = int(sys.argv[4])

# Initialize dictionaries for storing word frequencies
l = {}
g = {}

# Initialize counter for the number of lines processed
t = 0

# Open the input file
with open(input_file_name, 'r') as input_file:
    # Loop through each line of input
    for line in input_file:
        # Convert line to lowercase
        line = line.lower()
        # Replace dots with newline characters
        line = line.replace('.', '\n')
        # Remove all punctuation marks except dot and replace them with spaces
        line = re.sub(r'[^\w\s.]+', ' ', line)
        # Remove all numeric chars and replace them with spaces
        line = re.sub(r'[0-9]+', ' ', line)
        # Remove words starting with 'X' (remove trash)
        line = ' '.join(word for word in line.split() if not word.startswith('X'))

        # Increment line counter
        t += 1

        # Loop through each word in the line
        for word in line.split():
            # Increment frequency of word in line
            l[(t, word)] = l.get((t, word), 0) + 1
            # Increment frequency of word in entire text
            g[word] = g.get(word, 0) + 1

# Open the output file
with open(output_file_name, 'w') as output_file:
    # Loop through each word in the g dictionary
    for word in list(g.keys()):
        # Delete words with frequency outside the specified range
        if g[word] < min_frequency or g[word] > max_frequency:
            del g[word]
        else:
            # Write remaining words separated by spaces to the output file
            output_file.write(word + ' ')
    output_file.write('\n')

    # Loop through each line processed
    for i in range(1, t + 1):
        # Loop through each word in the g dictionary
        for word in list(g.keys()):
            # Write frequency of word in line to the output file
            output_file.write(str(l.get((i, word), 0)) + ' ')
        output_file.write('\n')

# Now, open the file in write mode and remove the last column using strip()
with open(output_file_name, "r+") as file:
    lines = file.readlines()
    file.seek(0)
    for line in lines:
        # Remove the last column by stripping the trailing whitespace
        file.write(line.rstrip() + '\n')
    file.truncate()

print("Word frequency calculation complete. Output saved to", output_file_name)

