book_text = get_book_text("books/frankenstein.txt")

def char_count(book_text):
    words = book_text.split()
    return len(words)