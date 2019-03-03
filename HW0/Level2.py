'''This is the function in modules.py'''
def get_coshow(contents):
    coshow_dict = {}  #declare coshow_dict as dictionary
    cat_content = ' '.join(contents)  #join the contents with space
    clean_content = remove_punctuation(cat_content)	#remove all punctuation in cat_content
    cut_content = jieba.lcut(clean_content)	#use jieba.lcut to cut the words
    cut_content = list(filter(lambda x: x!=' ', cut_content)) #remove all blank element
    for i in range(len(cut_content)-1):
        wcw = cut_content[i] + cut_content[i+1]
    #     print(wcw)
        try:
            coshow_dict[wcw] = coshow_dict[wcw] + 1
        except: #wcw does not exist in coshow_dict
            coshow_dict[wcw] = 1

    sdbv = sort_dict_by_values(coshow_dict)
    return sdbv