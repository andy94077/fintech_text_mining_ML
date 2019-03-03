#@@@ All revised sessions will be marked with 3 '@@@' above
import os
import pickle
import jieba
import operator
import statistics
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager as font_manager
from datetime import datetime
from collections import Counter

from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
from PIL import Image

#@@@ revise the with open(...) methods. This method is MUCH faster.
stopwords=np.loadtxt('../jieba_data/stopwords.txt',dtype=np.str,delimiter='\n', encoding='utf-8')
stopwords=np.char.strip(stopwords)
stopwords=np.append(stopwords,' ')


#@@@ abandon the replace method. That method is very slow because it will copy the string every time it was called.
import re,string
def remove_punctuation(content_string, user_pc=False):
    punc=r'[a-zA-Z'+string.punctuation+r'\r\xa0\u3000、，。「」！？；：]' if user_pc is False else user_pc
    return re.sub(punc,' ',content_string)

def get_coshow(contents):
    cat_content = ' '.join(contents)
    clean_content = remove_punctuation(cat_content)
    cut_content = np.array(jieba.lcut(clean_content)) #@@@ use numpy array
    cut_content = np.extract(cut_content!=' ',cut_content) #@@@filter the ' ' elements, and faster
    
    #@@@ The original for loop just iterates the elements, add the element with the next one, and then add it into the coshow_dict.
    #@@@ This can be implemented by numpy array easily. First we add the elements with the next elements, and then let Counter object count the number of occurrences. 
    #@@@ Finally, we return a list of items sorted by the value in Counter. 
    return Counter(np.char.add(cut_content[:-1], cut_content[1:])).most_common()


#@@@ code in the final_report
'''---------before---------'''
names = []
with open('../data/names.txt', 'r', encoding='utf-8-sig') as f:
    names = f.read().split('\n')
    
events = []
with open('../data/events.txt', 'r', encoding='utf-8-sig') as f:
    events = f.read().split('\n')
'''---------after---------'''
#@@@ the two lines below is much faster and shorter than the lines above
names = list(np.loadtxt('../data/names.txt', dtype=np.str, delimiter='\n', encoding='utf-8-sig'))
events = list(np.loadtxt('../data/events.txt', dtype=np.str, delimiter='\n', encoding='utf-8-sig'))
