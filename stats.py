def word_count(book_string):
    return len(book_string.split())

def character_count(book_string):
    char_dict = {}
    for char in book_string:
        current_char = char.lower()
        if current_char in char_dict:
            char_dict[current_char] += 1
        else:
            char_dict[current_char] = 1
    return char_dict

def count_report(char_dict):
    data_sorted= []
    for char in char_dict:
        if char.isalpha():
            data_sorted.append({"char": char, "num":char_dict[char]})
    data_sorted.sort(reverse=True,key=sort_count_report)
    return data_sorted


def sort_count_report(d):
    return d['num']
    pass
