import tkinter as tk
from tkinter import scrolledtext
from spell_checker import check_spelling
from grammar_checker import check_grammar

def process_text():
    input_text = text_input.get("1.0", tk.END).strip()
    words = input_text.split()

    # Spell Check
    spell_results = [check_spelling(word) for word in words]
    
    # Grammar Check
    grammar_result = check_grammar(input_text)

    # Display Results
    spell_output.delete("1.0", tk.END)
    spell_output.insert(tk.END, "\n".join(spell_results))

    grammar_output.delete("1.0", tk.END)
    grammar_output.insert(tk.END, grammar_result)

# GUI Setup
root = tk.Tk()
root.title("Sinhala Spell and Grammar Checker")

# Input Text Box
tk.Label(root, text="Enter Text:").pack()
text_input = scrolledtext.ScrolledText(root, height=10, width=50)
text_input.pack()

# Check Button
tk.Button(root, text="Check Text", command=process_text).pack()

# Spell Checker Output
tk.Label(root, text="Spell Checker Output:").pack()
spell_output = scrolledtext.ScrolledText(root, height=10, width=50)
spell_output.pack()

# Grammar Checker Output
tk.Label(root, text="Grammar Checker Output:").pack()
grammar_output = scrolledtext.ScrolledText(root, height=5, width=50)
grammar_output.pack()

root.mainloop()
