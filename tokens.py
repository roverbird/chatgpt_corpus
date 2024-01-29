import re
import csv
from collections import Counter

def calculate_word_frequency(file_path, output_path):
    # Read the content of the file
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()

    # Tokenize the text using a simple regex
    tokens = re.findall(r'\b\w+\b', text.lower())

    # Calculate word frequencies
    word_frequencies = Counter(tokens)

    # Total number of tokens
    total_tokens = len(tokens)

    # Calculate frequency per actual tokens and induced frequency per billion tokens
    result = []
    for word, frequency in word_frequencies.items():
        frequency_per_token = frequency / total_tokens
        frequency_per_billion_tokens = frequency_per_token * 1e9
        result.append((word, frequency, frequency_per_token, frequency_per_billion_tokens))

    # Sort the result by frequency in descending order
    result.sort(key=lambda x: x[1], reverse=True)

    # Write the result to a CSV file
    with open(output_path, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['Word', 'Frequency', 'Frequency per Token', 'Frequency per Billion Tokens']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        # Write the header
        writer.writeheader()

        # Write each row
        for word, frequency, freq_per_token, freq_per_billion in result:
            writer.writerow({
                'Word': word,
                'Frequency': frequency,
                'Frequency per Token': freq_per_token,
                'Frequency per Billion Tokens': freq_per_billion
            })

# Example usage: replace 'your_file.txt' and 'results.csv' with the actual file paths
calculate_word_frequency('/local-folder/EN/chat-gpt-EN.txt', 'gpt-results.csv')

