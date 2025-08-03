def get_num_words(book_string: str):
    num_words = book_string.split()
    return len(num_words)

def countCharacters(book_string: str):
    book_characters = list(book_string)
    character_dict = {}

    for character in book_characters:
        lower_cased_character = character.lower()
        if lower_cased_character in character_dict:
            character_dict[lower_cased_character] += 1
        else:
            character_dict[lower_cased_character] = 1
    print(character_dict)
    return character_dict

def chars_dict_to_sorted_list(char_counts):
    result = []
    for char, count in char_counts.items():
        if char.isalpha():
            result.append({"char": char, "num": count})
    result.sort(key = lambda item: item["num"], reverse=True)
    return result 
