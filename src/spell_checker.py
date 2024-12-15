from difflib import get_close_matches

# Load the dictionary
with open("../data/dictionary.txt", 'r', encoding='utf-8') as file:
    dictionary = file.read().splitlines()

# Function to check spelling and provide suggestions
def check_spelling(word):
    if word in dictionary:
        return f"'{word}' is correct."
    else:
        suggestions = get_close_matches(word, dictionary, n=3)
        if suggestions:
            return f"'{word}' is incorrect. Suggestions: {', '.join(suggestions)}"
        else:
            return f"'{word}' is incorrect. No suggestions."
