import json
import re
from collections import Counter

stop_words = {'i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', 'her', 'hers', 'herself', 'it', 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', 'should', 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', 'couldn', 'didn', 'doesn', 'hadn', 'hasn', 'haven', 'isn', 'ma', 'mightn', 'mustn', 'needn', 'shan', 'shouldn', 'wasn', 'weren', 'won', 'wouldn'}
A_word_count = Counter() 
B_word_count = Counter() 
E_word_count = Counter() 
V_word_count = Counter() 
temp = []
with open('trg.csv', 'r') as file:
    file.readline()
    for line in file:
        a = line.split(",")
        a[2] = a[2][1:-2]
        temp = [i for i in re.findall(r"[\w]+", a[2]) if i not in stop_words]
        
        if a[1] == "A":
            for i in temp:
                if i in A_word_count.keys():
                    A_word_count[i] += 1
                else:
                    A_word_count[i] = 1
        if a[1] == "B":
            for i in temp:
                if i in B_word_count.keys():
                    B_word_count[i] += 1
                else:
                    B_word_count[i] = 1
        if a[1] == "E":
            for i in temp:
                if i in E_word_count.keys():
                    E_word_count[i] += 1
                else:
                    E_word_count[i] = 1
        if a[1] == "V":
            for i in temp:
                if i in V_word_count.keys():
                    V_word_count[i] += 1
                else:
                    V_word_count[i] = 1

with open('Awordcount.json', 'w') as Af:
    json.dump(A_word_count, Af)

with open('Bwordcount.json', 'w') as Bf:
    json.dump(B_word_count, Bf)   
    
with open('Ewordcount.json', 'w') as Ef:
    json.dump(E_word_count, Ef)  
    
with open('Vwordcount.json', 'w') as Vf:
    json.dump(V_word_count, Vf)    
