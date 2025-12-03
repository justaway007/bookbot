from stats import word_count
from stats import character_count
from stats import count_report

def get_book_text(file_path):
    with open(file_path, encoding="utf-8-sig") as f:
        file_contents = f.read()
    return file_contents



def main():
    book_path = ('books/frankenstein.txt')
    my_book = get_book_text(book_path)
    my_word_count = word_count(my_book)
    my_report = count_report(character_count(my_book))
    my_report_print = ""
    for char_count in my_report:
        my_report_print += char_count['char'] + ': ' + str(char_count['num']) +'\n'
    my_report_print_final = my_report_print[:-1]
    report = f"""
============ BOOKBOT ============
Analyzing book found at {book_path}...
----------- Word Count ----------
Found {my_word_count} total words
--------- Character Count -------
{my_report_print_final}
============= END ===============
"""
    print(report)
    


main()