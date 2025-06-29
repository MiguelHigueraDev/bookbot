def count_words(text):
    return len(text.split())

def count_characters(text):
    counts = {}
    lowercase_text = text.lower()
    for word in lowercase_text:
        for letter in word:
            if letter in counts:
                counts[letter] += 1
            else:
                counts[letter] = 1
                
    return counts

def sort_char_counts(character_dict):
    return dict(sorted(character_dict.items(), key=lambda item: item[1], reverse=True))
