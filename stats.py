def  get_num_words(file_path):
    with open(file_path) as book:
        word_count = len(book.read().split())
        return(word_count)
        #print(f"{word_count} words found in the document")

def character_counter(file_path):
    character_count = {
                        "a": 0,
                        "b": 0,
                        "c": 0,
                        "d": 0,
                        "e": 0,
                        "f": 0,
                        "g": 0,
                        "h": 0,
                        "i": 0,
                        "j": 0,
                        "k": 0,
                        "l": 0,
                        "m": 0,
                        "n": 0,
                        "o": 0,
                        "p": 0,
                        "q": 0,
                        "r": 0,
                        "s": 0,
                        "t": 0,
                        "u": 0,
                        "v": 0,
                        "w": 0,
                        "x": 0,
                        "y": 0,
                        "z": 0
                        }
    with open(file_path) as book:
        for character in list(book.read().lower()):
            if character in character_count:
                character_count[character] += 1
    #count_string = ""
    #for letter in character_count:
    #    count_string += f"'{letter}': {character_count[letter]}\n"
    #print(count_string)
    return character_count

def sort_on(items):
    return items["num"]

def sort_dict_to_list(character_dict):
    character_list = []
    for i in character_dict:
        character_list.append({"char": i, "num": character_dict[i]})
    character_list.sort(reverse=True, key=sort_on)
    return character_list