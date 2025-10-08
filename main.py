from stats import get_num_words
from stats import get_each_char_count
from stats import get_sorted_list
import sys
def main():
    if len(sys.argv)<2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    content=get_book_text(sys.argv[1])
    num_words=get_num_words(sys.argv[1])
    print(f"Found {num_words} total words")
    count_of_each_char=get_each_char_count(sys.argv[1])
    print("--------- Character Count -------")
    sorted_list=get_sorted_list(count_of_each_char)
    for item in sorted_list:
        if item["char"].isalpha():
             print(f"{item["char"]}: {item["num"]}")
    print("============= END ===============")

def get_book_text(filepath):
    with open(filepath) as f:
    	return f.read()
def char_count(file_contents):
    file_contents_char_dict = {}
    file_contents_char_list = list(file_contents.lower())
    file_contents_char_set = set(file_contents_char_list)
    file_contents_char_unique = list(file_contents_char_set)
    for char in file_contents_char_list:
        if char in file_contents_char_dict:
            file_contents_char_dict[char]+=1
        else:
            file_contents_char_dict[char]=1
    return file_contents_char_dict
main()
