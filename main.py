import sys
from stats import get_num_words, sort_dict_to_list, character_counter

def main(file_path):
    word_count = get_num_words(file_path)
    sorted_list = sort_dict_to_list(character_counter(file_path))
    print("============ BOOKBOT ============\n" \
    "Analyzing book found at books/frankenstein.txt...\n" \
    "----------- Word Count ----------\n" \
    f"Found {word_count} total words\n" \
    "--------- Character Count -------"
    )
    for i in sorted_list:
        print(f"{i["char"]}: {i["num"]}")
    print("============= END ===============")

try:
    book_path = sys.argv[1]
    main(book_path)
except IndexError:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
except Exception as e:
    print(f"Error code: {e}")
    sys.exit(1)