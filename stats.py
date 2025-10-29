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

def sorted_count(count):
    sorted = []
    for char, num in count.items():
        if not char.isalpha():
            continue
        sorted.append({"char": char, "num": num})
    sorted.sort(reverse=True, key=sort_on)
    final_list = []
    for item in sorted:
        final_list.append(f"{item["char"]}: {item["num"]}")
    return final_list