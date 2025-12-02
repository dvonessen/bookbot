import sys

from stats import get_num_char, get_num_words, sort_by_count


def get_book_text(path: str) -> str:
    with open(path) as f:
        return f.read()


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    txt = get_book_text(book_path)
    word_count = get_num_words(txt)
    sorted = sort_by_count(get_num_char(txt))
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for i in sorted:
        if i["char"].isalpha():
            print(f"{i['char']}: {i['num']}")
    print("============= END ===============")


if __name__ == "__main__":
    main()
