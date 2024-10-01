def main():
    book_path ="books/frankenstein.txt"
    text = get_text(book_path)
    num_words = get_num_words(text)
    
    num_chars_dict = get_num_chars(text)
    #print(num_chars_dict)
    sorted_chars_list =  list_dict(num_chars_dict)
    

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words} words found in the document \n")

    for i in sorted_chars_list:
        if i['char'].isalpha():
            print(f"The '{i['char']}'character was found {i['num']} times")
        else:
            continue

    print("--- End report ---")

def get_text(path):
    with open(path) as f:
        return f.read()

def get_num_words(text):
    words = text.split()
    return len(words)
    
def get_num_chars(text):
    lowered_text = text.lower()
    letter_count = {}
    for i in lowered_text:
        if i in letter_count:
            letter_count[i] += 1
        else:
            letter_count[i] = 1
    return letter_count
        
def list_dict(num_chars_dict):
    dict_list = []
    for c in num_chars_dict:
        dict_list.append({"char": c, "num": num_chars_dict[c]})
    dict_list.sort(reverse = True, key = sort_on)
    return dict_list

def sort_on(dict):
    return dict["num"]

main()