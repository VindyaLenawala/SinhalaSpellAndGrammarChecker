from spell_checker import check_spelling
from grammar_checker import check_grammar

def check_text(text):
    print("Spell Checking:")
    for word in text.split():
        print(check_spelling(word))
    
    print("\nGrammar Checking:")
    print(check_grammar(text))

if __name__ == "__main__":
    test_text = "මම යනවයි."
    check_text(test_text)