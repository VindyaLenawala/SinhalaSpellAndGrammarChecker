def check_grammar(sentence):
    # Predefined grammar rules
    rules = {
        "මම": ["යනවා", "කතා කරනවා"],
        "ඔබ": ["ගියා", "කියනවා"],
        "අපි": ["යමු", "කතා කරනවා"]
    }

    words = sentence.split()
    for i, word in enumerate(words[:-1]):
        if word in rules:
            if words[i + 1] not in rules[word]:
                return f"Grammar error: '{word} {words[i + 1]}' is incorrect."
    return "No grammar errors detected."