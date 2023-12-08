def main():
    book_url = "books/frankenstein.txt"
    text = get_book_text(book_url)
    words = get_words_from_text(text)
    num_chars = get_chars_in_text(text)

    generate_book_report(book_url, words, num_chars)

def get_book_text(book_url):
    with open(book_url) as f:
        return f.read()
        
def get_words_from_text(text):
    return len(text.split())

def get_chars_in_text(text):
    chars = {}
    for char in text.lower():
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1
    return chars

def sort_on(d):
    return d["num"]

def generate_chars_list(num_chars):
    sorted_list = []
    for char in num_chars:
        sorted_list.append({"char": char, "num": num_chars[char]})
    
    sorted_list.sort(reverse=True, key=sort_on)

    return sorted_list

def generate_book_report(book_url, words, num_chars):
    print(f"--- Begin report of {book_url} ---")
    print(f"{words} words found in the document")
    print()

    sorted_chars_list = generate_chars_list(num_chars)

    for item in sorted_chars_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' was found {item['num']} times")
    print("--- End report ---")


main()
