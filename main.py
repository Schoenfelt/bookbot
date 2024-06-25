def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    print(text)
    word_count = count_words(text)
    print(f"{word_count} words found in the document.")

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def count_words(text_string):
    words = text_string.split()
    return len(words)
main()