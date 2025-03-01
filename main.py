import sys
from stats import get_num_words
from stats import get_char_counts
from stats import sorted_list

def main():

    #    print(get_book_text("./books/frankenstein.txt"))

    book = "books/frankenstein.txt"

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
    else:
        book = sys.argv[1]
    num_words = get_num_words(get_book_text(book))
        
    count_chars = get_char_counts(get_book_text(book))
    sortted = sorted_list(count_chars)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for d in sortted:
        print(f"{d["char"]}: {d["num"]}")
    print("============= END ===============")        
        
    return



def get_book_text(filepath):
    file_contents = ""
    with open(filepath) as f:
        file_contents = f.read()

    return file_contents

main()