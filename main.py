from stats import get_num_words, get_char_dict

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    char_count = get_char_dict(text)
    print(f"{num_words} words found in the document.")
    for key in char_count:
        print(f"'{key}': {char_count[key]}")

def get_book_text(path):
    with open(path) as f:
        return f.read()

main()