import re

def read_bigrams(file_path):
    with open(file_path, 'r', encoding='utf-8') as bigrams_file:
        return set(line.strip() for line in bigrams_file)

def clean_text(text):
    # Convert to lowercase and replace punctuation with spaces
    cleaned_text = re.sub(r'[^\w\s]', ' ', text.lower())
    return cleaned_text

def count_tokens(text):
    # Use regex to split words
    words = re.findall(r'\b\w+\b', text)
    return len(words)

def count_matching_bigrams(text, bigrams):
    # Use regex to find bigrams
    bigram_matches = re.findall(r'\b\w+\s\w+\b', text)
    return sum(1 for bigram in bigram_matches if bigram in bigrams)

# File paths
input_file_path = 'input.txt'
bigrams_file_path = 'bigrams.txt'
output_file_path = 'output_stats06.txt'

# Read bigrams from bigrams.txt
bigrams = read_bigrams(bigrams_file_path)

# Read input text from input.txt, clean it, and convert to lowercase
with open(input_file_path, 'r', encoding='utf-8') as input_file:
    input_text = input_file.read()
    cleaned_input_text = clean_text(input_text)

# Count tokens in input.txt
num_tokens = count_tokens(cleaned_input_text)

# Count matching bigrams
num_matching_bigrams = count_matching_bigrams(cleaned_input_text, bigrams)

# Calculate percentage of matching bigrams
percentage_matching_bigrams = (num_matching_bigrams / len(bigrams)) * 100 if len(bigrams) > 0 else 0

# Write results to output.txt
with open(output_file_path, 'w') as output_file:
    output_file.write(f'Number of tokens in input.txt: {num_tokens}\n')
    output_file.write(f'Number of bigrams from bigrams.txt found in input.txt: {num_matching_bigrams}\n')
    output_file.write(f'Percentage of bigrams found in input.txt: {percentage_matching_bigrams:.2f}%\n')

