from stats import word_counter, letter_counter, sort_dict
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        text=f.read()
    return text

def main():
    count = word_counter(get_book_text(sys.argv[1]))
    letter_dict = letter_counter(get_book_text(sys.argv[1]))
    sorted_dict =(sort_dict(letter_dict))

    print("============ BOOKBOT ============")
    print("Analyzing book found at " + sys.argv[1])
    print("----------- Word Count ----------")
    print(f'Found {count} total words')
    print("----------- Letter Count ----------")
    for x in sorted_dict:
        if x[0].isalpha():
            print(f'{x[0]}: {x[1]}')
    print("==============END=================")
    
if __name__ == "__main__":
    main()

