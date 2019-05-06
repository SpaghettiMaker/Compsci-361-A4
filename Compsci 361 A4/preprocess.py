import json
import re
from collections import Counter

# frequent meaningless words from nltk
stop_words = {'i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', 'her', 'hers', 'herself', 'it', 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', 'should', 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', 'couldn', 'didn', 'doesn', 'hadn', 'hasn', 'haven', 'isn', 'ma', 'mightn', 'mustn', 'needn', 'shan', 'shouldn', 'wasn', 'weren', 'won', 'wouldn'}

word_count = [Counter(), Counter(), Counter(), Counter()] # A, B, E, V
super_dict = Counter()
temp = []
classes = ["A", "B", "E", "V"]
# attempt inverse document feq
with open('trg.csv', 'r') as file:
    file.readline() # ignore first line (id,class,abstract)
    for line in file:
        a = line.split(",")
        a[2] = a[2][1:-2] # remove ""
        temp = [i for i in re.findall(r"[\w]+", a[2]) if i not in stop_words]

        flag = 0 
        # if key exists i.e. word has occured before add one to value else init with word=key, value=1
        index_num = classes.index(a[1])
        for i in temp:
            if flag == 0: # down weight words if the occur in lots of different abstracts
                if i not in super_dict.keys():
                    super_dict[i] = 1
                else: 
                    super_dict[i] += 1
            flag = 1
            if i in word_count[index_num].keys():
                word_count[index_num][i] += 1
            else:
                word_count[index_num][i] = 1

with open('Awordcount.json', 'w') as Af:
    json.dump(word_count[0], Af)

with open('Bwordcount.json', 'w') as Bf:
    json.dump(word_count[1], Bf)   
    
with open('Ewordcount.json', 'w') as Ef:
    json.dump(word_count[2], Ef)  
    
with open('Vwordcount.json', 'w') as Vf:
    json.dump(word_count[3], Vf) 
    
with open('Supercount.json', 'w') as Sf:
    json.dump(word_count[0], Sf)
