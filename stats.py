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
        data_sorted.append({"char": char, "num":char_dict[char]})
    return sort_count_report(data_sorted)

def sort_count_report(data):
    data_sorted = []
    numbers = []
    for d in data:
        numbers.append(d['num'])
    numbers.sort(reverse=True)
    for n in numbers:
        for d in data:
            if d['num'] == n and d['char'].isalpha():
                data_sorted.append(d)
    return data_sorted