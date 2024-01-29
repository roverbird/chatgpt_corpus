import re
import csv
import statistics
from collections import Counter

def clean_text(text):
    # Convert to lowercase and replace punctuation with spaces
    cleaned_text = re.sub(r'[^\w\s]', ' ', text.lower())
    return cleaned_text

def calculate_word_frequencies(text):
    # Use regex to split words
    words = re.findall(r'\b\w+\b', text)
    return Counter(words)

def read_csv(file_path):
    with open(file_path, 'r', newline='', encoding='utf-8') as csv_file:
        csv_reader = csv.reader(csv_file)
        header = next(csv_reader)
        data = {row[0]: row[1] for row in csv_reader}
    return header, data

# File paths
input_file_path = 'input.txt'
output_csv_file_path = 'output.csv'
gutenberg_csv_file_path = 'project-gutenberg-word-frequency-list-2006.csv'

# Read input text from input.txt, clean it, and convert to lowercase
with open(input_file_path, 'r', encoding='utf-8') as input_file:
    input_text = input_file.read()
    cleaned_input_text = clean_text(input_text)

# Count tokens in input.txt
num_tokens = len(cleaned_input_text.split())

# Calculate word frequencies for input.txt
input_word_frequencies = calculate_word_frequencies(cleaned_input_text)

# Read data from project-gutenberg-word-frequency-list-2006.csv
gutenberg_header, gutenberg_data = read_csv(gutenberg_csv_file_path)

# Write results to output.csv
with open(output_csv_file_path, 'w', newline='') as output_csv_file:
    csv_writer = csv.writer(output_csv_file)
    csv_writer.writerow(['Word', 'PerBillion', 'GutenbergPerBillion', 'Ratio'])

    ratios = []  # to store all calculated ratios

    for word, frequency in input_word_frequencies.items():
        relative_frequency = frequency / num_tokens
        relative_frequency_per_billion = relative_frequency * 1e9

        # Check if the word is in the gutenberg data
        if word in gutenberg_data:
            gutenberg_per_billion = float(gutenberg_data[word])
            ratio = relative_frequency_per_billion / gutenberg_per_billion
            csv_writer.writerow([word, relative_frequency_per_billion, gutenberg_per_billion, ratio])
            ratios.append(ratio)

    # Calculate and write the median and variance at the end of the output.csv file
    median_ratio = statistics.median(ratios)
    # variance_ratio = statistics.variance(ratios)
    
    csv_writer.writerow(['Median Ratio', '', '', median_ratio])
    # csv_writer.writerow(['Variance Ratio', '', '', variance_ratio])

