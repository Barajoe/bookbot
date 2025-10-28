import string

def get_book_text(filepath):
    with open (filepath, encoding="utf-8") as f:
        file_contents = f.read()
        return file_contents

book_text = get_book_text("books/frankenstein.txt")
punctuation_remove = ["'", "-"]

def char_count(book_text):
    words = book_text.split()
    return len(words)

def main():
    print(f"Found {char_count(book_text)} total words")

main()