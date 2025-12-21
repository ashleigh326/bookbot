def number_of_words(text):
    number = 0
    words = text.split()
    return len(words)

def number_of_characters(text):
    char_dict = {}

    for char in text:
        lowered_char = char.lower()
        if lowered_char not in char_dict:
            char_dict[lowered_char] = 1
        else:
            char_dict[lowered_char] += 1

    return char_dict

def sort_on(item):
    return item["num"]

def sort_dictionary(characters_count):
    dict_list = []
    for char in characters_count:
        temp_dict = {"char": char, "num" : characters_count[char]}
        dict_list.append(temp_dict)
    
    dict_list.sort(reverse=True, key=sort_on)

    return dict_list