def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()


def get_num_words(text):
    textList = text.split()
    num_words = len(textList)
    return num_words


def count_characters(text):
    dictionary = {}
    for ch in text:
        character = ch.lower()
        if character not in dictionary:
            dictionary[character] = 1
        else:
            dictionary[character] += 1

    return dictionary


def sort_on(items):
    return items["num"]


def sorted_characters_list(count_dictionary):
    list = []
    for character, num in count_dictionary.items():
        list.append({"char": character, "num": num})
    list.sort(reverse=True, key=sort_on)
    return list
