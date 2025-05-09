from stats import word_count
from stats import word_by_word
from stats import report
import sys
def get_book_text(filepath):
    with open(filepath, encoding="utf8") as f:
        file_contents = f.read()
        return file_contents
def main():
    if len(sys.argv)<2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    text = get_book_text(sys.argv[1])
    number_words=word_count(text)
    words=word_by_word(text)
    words2=report(words)
    valu=list(words2.values())
    ke=list(words2.keys())
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {number_words} total words")
    print("--------- Character Count -------")
    for i in range(len(valu)):
        if valu[i]>0:
            print(f"{ke[i]}: {valu[i]}")
    print("============= END ===============")
main()