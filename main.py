def main():
    book_path = 'books/frankenstein.txt'
    book_contents = get_book_text(book_path)
    # print(book_contents)
    word_count = get_book_word_length(book_contents)
    # print(word_count)

    word_dict = get_word_dictionary(book_contents)

    char_fraises = get_character_fraises(word_dict)

    # print(word_dict)
    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in the document\n")
    for fraise in char_fraises:
        print(fraise)
   

def sort_on(dict):
    return dict["count"]

def get_character_fraises(word_dict):
    char_list = []
    for char, count in word_dict.items():
        if char.isalpha():
            char_list.append({"char": char, "count": count})

    char_list.sort(reverse=True, key=sort_on)

    return_value = []
    for item in char_list:
        return_value.append(f"The '{item['char']}' character was found {item['count']} times")
    return return_value


def get_book_word_length(book_contents):
    return len(book_contents.split())

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()

def get_word_dictionary(book_contents):
    word_list = book_contents.lower()
    word_dict = {}
    for word in word_list:
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1
    return word_dict
    

main()