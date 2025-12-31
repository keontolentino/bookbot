def count_words(filepath):
    with open(filepath) as f:
        content = f.read()
        words = content.split()
    num_words = 0
    for word in words:
        num_words += 1
    print(f"Found {num_words} total words")

def count_char(filepath):
    with open(filepath) as f:
        content = f.read()
        

    count = {}
    for c in content.lower():
        if c in count:
            count[c] += 1
        else:
            count[c] = 1
    return count

def sort_count(dictionary):
    cnt_chr = dictionary
    lst = []
    char_lst = []
    num_lst = []
    for key in cnt_chr:
        char_lst.append(key)
        num_lst.append(cnt_chr[key])
    

    for i in range(len(char_lst)):
        dct = {}
        if char_lst[i].isalpha():
            dct = {"char":char_lst[i], "num":num_lst[i]}
            lst.append(dct)
        else: 
            continue
    
    def get_num(dct):
        return dct["num"]
        
    lst.sort(key=get_num, reverse = True)


    return lst


    