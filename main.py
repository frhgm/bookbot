def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    # print(chars_dict)
    report(chars_dict)


def get_num_words(text):
    words = text.split()
    return len(words)


def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars


def get_book_text(path):
    with open(path) as f:
        return f.read()


def report(dictionary):
    ini = '--- Begin report of books/frankenstein.txt ---'
    end = '--- End report ---'

    dictionary = dict(
        sorted(dictionary.items(), reverse=True, key=lambda item: item[1]))

    for d in dictionary:
        if d.isalpha():
            value = dictionary[d]
            print(template(d, dictionary[d]))


def template(char, times):
    temp = f"The '{char}' character was found {times} times"

    return temp


main()
