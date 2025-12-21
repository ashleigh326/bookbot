import sys
from stats import number_of_words, number_of_characters, sort_dictionary

def get_book_text(file_path):
    contents = ""
    with open(file_path) as f:
        contents = f.read()
    return contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    text = get_book_text(sys.argv[1])
    print(text)

    word_count = number_of_words(text)
    print(f"Found {word_count} total words")

    characters_count = number_of_characters(text)
    print(characters_count)

    sorted_character_count = sort_dictionary(characters_count)
    print(sorted_character_count)

    for i in sorted_character_count:
        if i["char"].isalpha():
            print(f"{i["char"]}: {i["num"]}")
    
main()

