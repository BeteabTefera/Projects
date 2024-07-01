'''
    write a python function to count the number of unique words
    and how often each occurs

    Input: path to a text file
    Output:
    - Total number of words
    - top 20 most frequent words
    - number of occurences for top 20

'''
import re
from operator import itemgetter
def count_words(filePath):
    lines = []
    with open(filePath,'r',encoding="utf8") as file:
        lines = [[word for word in re.sub("[^A-Za-z]", " ",sentence.strip().lower()).split(' ') if word.isalpha()]
                 for sentence in file.readlines() if sentence != '\n']
    # for sentence in lines:
    dic = {}
    for wordslist in lines:
        for word in wordslist:
            if word in dic:
                dic[word] += 1
            else:    
                dic[word] = 1
    res = dict(sorted(dic.items(),key=itemgetter(1),reverse=True)[:len(lines)-1])
    pair = list(res.items())[:21]
    print('TOP 20 UNIQUE WORDS\nWords\tCount')
    for key,value in pair:
        print(f'{key}\t{value}')
        

    
count_words(filePath)
