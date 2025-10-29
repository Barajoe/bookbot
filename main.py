from stats import char_count

def get_book_text(filepath):
    with open (filepath, encoding="utf-8") as f:
        file_contents = f.read()
        return file_contents

book_text = get_book_text("books/frankenstein.txt")

def main():
    print(f"Found {stats.char_count(book_text)} total words")

main()