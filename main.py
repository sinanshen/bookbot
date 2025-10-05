from stats import get_num_words, get_book_text, count_characters, sorted_characters_list
import sys


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        for argv in sys.argv:
            if argv == "main.py":
                continue
            else:
                bookText = get_book_text(argv)
                countCharacters = count_characters(bookText)
                sorted_list = sorted_characters_list((countCharacters))
                print("============ BOOKBOT ============")
                print(f"Analyzing book found at {argv}...")
                print("----------- Word Count ----------")
                print(f"Found {get_num_words(argv)} total words")
                print("--------- Character Count -------")
                for item in sorted_list:
                    ch = item["char"]
                    if ch.isalpha():
                        print(f"{ch}: {item['num']}")
                print("============= END ===============")


main()
