from itertools import combinations
from collections import Counter
import string

def clean_text(text):
    # Convert to lowercase and remove punctuation and numerals
    translator = str.maketrans(' ', ' ', string.punctuation + string.digits)
    cleaned_text = text.lower().translate(translator)
    return cleaned_text

def extract_ngrams(text, n):
    words = text.split()
    ngrams = zip(*[words[i:] for i in range(n)])
    return [' '.join(gram) for gram in ngrams]

# Read keywords from keywords.txt
with open('keywords.txt', 'r') as keywords_file:
    keywords = set(keywords_file.read().split())

# Read input text from input.txt and clean it
with open('chatgpt-clean-corpus.txt', 'r') as input_file:
    input_text = input_file.read()
    cleaned_input_text = clean_text(input_text)

# Extract 3-grams and 2-grams containing words from keywords.txt
#four_grams = extract_ngrams(cleaned_input_text, 4)
#three_grams = extract_ngrams(cleaned_input_text, 3)
two_grams = extract_ngrams(cleaned_input_text, 2)

#filtered_four_grams = [gram for gram in four_grams if any(keyword in gram for keyword in keywords)]
#filtered_three_grams = [gram for gram in three_grams if any(keyword in gram for keyword in keywords)]
filtered_two_grams = [gram for gram in two_grams if any(keyword in gram for keyword in keywords)]

# Count occurrences of each 3-gram and 2-gram
#four_gram_counts = Counter(filtered_four_grams)
#three_gram_counts = Counter(filtered_three_grams)
two_gram_counts = Counter(filtered_two_grams)

# Filter out n-grams with frequency <= 3
cutoff_frequency = 30
#filtered_four_grams = {gram: count for gram, count in four_gram_counts.items() if count > cutoff_frequency}
#filtered_three_grams = {gram: count for gram, count in three_gram_counts.items() if count > cutoff_frequency}
filtered_two_grams = {gram: count for gram, count in two_gram_counts.items() if count > cutoff_frequency}

# Write output to output.txt in comma-separated format
with open('output.csv', 'w') as output_file:

#    for gram, count in filtered_four_grams.items():
#        output_file.write(f'{gram}, {count}\n')

#    for gram, count in filtered_three_grams.items():
#        output_file.write(f'{gram}, {count}\n')

    for gram, count in filtered_two_grams.items():
        output_file.write(f'{gram}, {count}\n')

