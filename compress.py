import os

# contatenate all files in dir to single txt file, stretch each file into one line, so that each line is a file
# remove noise

def process_txt_files(directory):
    output_file_path = os.path.join(directory, 'output.txt')
    with open(output_file_path, 'w', encoding='utf-8') as output_file:
        for filename in sorted(os.listdir(directory)):
            if filename.endswith('.txt'):
                input_path = os.path.join(directory, filename)

                # Read the content of the file
                with open(input_path, 'r', encoding='utf-8') as file:
                    content = file.readlines()

                # Remove the first 4 lines and the last 24 lines
                modified_content = content[4:-24]

                # Concatenate the lines into a single line
                concatenated_line = ''.join(modified_content).replace('\n', ' ').replace('\r', ' ')

                # Write the concatenated line to the output file
                output_file.write(concatenated_line + '\n')

                print(f"Processed: {input_path}")

    print(f"Concatenated content saved to: {output_file_path}")

if __name__ == "__main__":
    txt_directory = '/shitposts/EN'
    process_txt_files(txt_directory)

