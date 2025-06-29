def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def count_words(text):
    return len(text.split())
        
def main():
    text = get_book_text("books/frankenstein.txt")
    num_words = count_words(text)
    print(f"{num_words} words found in the document")
    
main()