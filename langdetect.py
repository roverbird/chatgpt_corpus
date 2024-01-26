import os
from langdetect import detect

# detect if each text file in dir contains text in English, mark such files with EN- in filename

def detect_language(text):
    try:
        language = detect(text)
        return language
    except:
        return "Unknown"

def process_txt_files(directory):
    for filename in os.listdir(directory):
        if filename.endswith('.txt'):
            input_path = os.path.join(directory, filename)

            # Read the content of the file
            with open(input_path, 'r', encoding='utf-8') as file:
                content = file.read()

            # Detect the language of the content
            language = detect_language(content)

            if language == "en":
                # If the detected language is English, rename the file
                new_filename = f'EN-{filename}'
                output_path = os.path.join(directory, new_filename)
                os.rename(input_path, output_path)

                print(f"Renamed: {input_path} -> {output_path}")
            else:
                print(f"Ignored: {input_path} (Language: {language})")

if __name__ == "__main__":
    txt_directory = '/media/sanka/Backup/shitposts/local-directory0'
    process_txt_files(txt_directory)

