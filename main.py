from stats import count_words
from stats import count_characters
import sys


def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()
        
def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    path = sys.argv[1]
    text = get_book_text(path)
    num_words = count_words(text)
    character_counts = count_characters(text)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for char in character_counts:
        if char.isalpha():
            count = character_counts[char]
            print(f"{char}: {count}")
    print("============= END ===============")
    
main()