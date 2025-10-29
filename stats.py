def word_count(book_text):
    words = book_text.split()
    return len(words)

def char_count(book_text):
    chars = book_text.lower()
    all_chars = dict()
    for char in chars:
        all_chars[char] = all_chars.get(char, 0) + 1
    return all_chars

def get_book_text(filepath):
    with open (filepath, encoding="utf-8") as f:
        file_contents = f.read()
        return file_contents

def sort_on(items):
    return items["num"]

book_text = get_book_text("books/frankenstein.txt")
count = char_count(book_text)

def sorted_count(count):
    sorted = []
    for char in count:
        if char == str:
            sorted.update({"char": char})
        else:
            sorted.update({"num": char})
    sorted.sort(reverse=True, key=sort_on)
    return sorted