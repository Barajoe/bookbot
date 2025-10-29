from stats import word_count, char_count, sort_on, sorted_count
import sys

if len(sys.argv) != 2:
    sys.stdout.write("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text(filepath):
    with open (filepath, encoding="utf-8") as f:
        file_contents = f.read()
        return file_contents

book_text = get_book_text(sys.argv[1])
count = char_count(book_text)

def main():
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count(book_text)} total words")
    print("--------- Character Count -------")
    print(sorted_count(count))
    print("============= END ===============")



main()