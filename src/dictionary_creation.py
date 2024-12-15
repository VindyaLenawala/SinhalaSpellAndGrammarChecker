import os
from nltk.tokenize import word_tokenize

# Paths for text files and dictionary
TEXT_FOLDER = "../data"
DICTIONARY_FILE = "../data/dictionary.txt"

# Extract words from all .txt files
def extract_words_from_files(folder_path):
    all_words = set()
    for file_name in os.listdir(folder_path):
        if file_name.endswith(".txt"):
            file_path = os.path.join(folder_path, file_name)
            with open(file_path, 'r', encoding='utf-8') as file:
                text = file.read()
                words = word_tokenize(text)  # Tokenize words
                all_words.update(words)
    return sorted(all_words)

# Save extracted words to dictionary file
def save_dictionary(words, output_file):
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write("\n".join(words))
    print(f"Dictionary saved to {output_file}")

if __name__ == "__main__":
    words = extract_words_from_files(TEXT_FOLDER)
    save_dictionary(words, DICTIONARY_FILE)
