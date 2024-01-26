import os
from bs4 import BeautifulSoup

# Parse downloaded html files, extract only text in paragraphs

def extract_text_from_html(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    paragraphs = soup.find_all('p')
    return '\n'.join(paragraph.get_text(separator='\n') for paragraph in paragraphs)

def process_html_files(directory):
    file_counter = 111  # Starting number for output files
    for filename in os.listdir(directory):
        input_path = os.path.join(directory, filename)
        output_path = os.path.join(directory, f'{file_counter}.txt')

        with open(input_path, 'r', encoding='utf-8') as file:
            html_content = file.read()

        extracted_text = extract_text_from_html(html_content)

        with open(output_path, 'w', encoding='utf-8') as output_file:
            output_file.write(extracted_text)

        print(f"Processed: {input_path} -> {output_path}")

        file_counter += 1

if __name__ == "__main__":
    html_directory = '/local-directory'
    process_html_files(html_directory)

