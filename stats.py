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