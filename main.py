import sys
from stats import word_counter
from stats import character_counter
from stats import dictor_format

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)


path = sys.argv[1]

def get_book_text(file_to_path):
    with open(file_to_path) as f:
        file_content = f.read()
        return str(file_content)


def word_counter(string):
    list = string.split()
    count = len(list)
    return count

def main():
    
    opened = get_book_text(path)
    #print(opened)
    tick = word_counter(opened)
    boom = character_counter(opened)
    dictor_format(tick, boom, path)


main()


