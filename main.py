def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    #print(text)
    word_count = get_count_words(text)
    #print(f"{word_count} words found in the document.")
    characters = get_char_count(text)
    #print(characters)
    sort_chars = sort_letter(characters)
    #print(sort_chars)

    print(f"---Begin report of {book_path}---")
    print(f"{word_count} words found in the document.")
    print()

    for item in sort_chars:
        print(f"The '{item['char']}' character was found {item['num']} times")

    print("--- End report ---")

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def get_count_words(text_string):
    words = text_string.split()
    return len(words)

def get_char_count(text):
    char_dict = {}
    for char in text:
        low_char = char.lower()
        if low_char in char_dict:
            char_dict[low_char] += 1
        else:
            char_dict[low_char] = 1
    return char_dict

def sort_on(d):
    return d["num"]

def sort_letter(char_dict):
    sorted_dict = []
    for c in char_dict:
        if c.isalpha():
            sorted_dict.append({"char": c, "num": char_dict[c]})
    sorted_dict.sort(reverse=True, key=sort_on)
    return sorted_dict
main()