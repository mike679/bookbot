def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    words = file_contents.split()
    print(f"{len(words)} words found in the document")
    
    file_contents_char_dict=char_count(file_contents)
    for char in file_contents_char_dict:
        if char.isalpha():
            print(f"The '{char}' character was found {file_contents_char_dict[char]} times")


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