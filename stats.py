def get_num_words(filepath):
    with open(filepath) as f:
        content=f.read()
    content_words=content.split()
    return(len(content_words))


def get_each_char_count(filepath):
    with open(filepath) as f:
        content=f.read()
    content_lo=content.lower()
    content_char_dict={}
    for char in content_lo:
        if char not in content_char_dict :
            content_char_dict[char]=1
        else:
            content_char_dict[char]+=1
    return content_char_dict    

def get_sorted_list(dict):
    list=[]
    for key,value in dict.items():
        list.append({"char":key, "num":value})
    list.sort(reverse=True,key=sort_basedon_part)
    return list
def sort_basedon_part(item):
    return item["num"]

