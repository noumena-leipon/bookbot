import sys
from stats import get_book_text, count_words, count_alphas, sort_alphas


def main():
    path = filename
    text = get_book_text(path)
    count = count_words(text)
    alphas = count_alphas(text)
    char_list = sort_alphas(alphas)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {count} total words.")
    print("--------- Character Count -------")
    for item in char_list:
        if item["char"].isalpha():
            print(f"{item['char']}: {item['count']}")
    print("============= END ===============")


arguments = sys.argv[0:]
filename = []

if len(arguments) < 2 or len(arguments) > 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    filename = arguments[1]

main()
