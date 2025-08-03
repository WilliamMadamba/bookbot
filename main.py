import sys
from stats import get_num_words, countCharacters, chars_dict_to_sorted_list

def main():
        if len(sys.argv) != 2:
            print("Usage: python3 main.py <path_to_book>")
            sys.exit(1)

        book = sys.argv[1]

        with open(book) as f:
                file_contents = f.read()
                num_words = get_num_words(file_contents)
                count_of_characters = countCharacters(file_contents)
                sorted_char_counts = chars_dict_to_sorted_list(count_of_characters)

                print("============ BOOKBOT ============")
                print(f"Analyzing book found at {book}...")
                print("----------- Word Count ----------")
                print(f"Found {num_words} total words")
                print("--------- Character Count -------")

                for item in sorted_char_counts:
                    char = item["char"]
                    num = item["num"]
                    print(f"{char}: {num}")

                print("============= END ===============") 

main()
