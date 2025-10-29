from stats import word_count, char_count, sort_on, sorted_count

def get_book_text(filepath):
    with open (filepath, encoding="utf-8") as f:
        file_contents = f.read()
        return file_contents

book_text = get_book_text("books/frankenstein.txt")
count = char_count(book_text)

def main():
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {word_count(book_text)} total words")
    print("--------- Character Count -------")
    print(sorted_count(count))
    print("============= END ===============")

main()