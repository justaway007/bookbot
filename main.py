from stats import word_count
from stats import character_count

def get_book_text(file_path):
    with open(file_path, encoding="utf-8-sig") as f:
        file_contents = f.read()
    return file_contents


def main():
    my_book = get_book_text('./books/frankenstein.txt')
    my_word_count = word_count(my_book)
    #print(f'Found {my_word_count} total words')
    print(character_count(my_book))



main()