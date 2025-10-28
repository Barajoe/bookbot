import string

def get_book_text(filepath):
    with open (filepath, encoding="utf-8") as f:
        file_contents = f.read()
        return file_contents

book_text = get_book_text("books/frankenstein.txt")
punctuation_remove = ["'", "-"]

def char_count(book_text):
    book_text = book_text.replace("\u00a0", " ")
    book_text = (
        book_text
        .replace("‘", "'")
        .replace("’", "'")
        .replace("“", '"')
        .replace("”", '"')
        .replace("—", " ")
        .replace("–", " ")
    )
    cleaned_text = ""
    for char in book_text:
        if char in string.punctuation:
            if char in punctuation_remove:
                char = ""
            else:
                char = " "
        cleaned_text += char
    words = cleaned_text.split()
    return len(words)

def main():
    print(f"Found {char_count(book_text)} total words")

main()