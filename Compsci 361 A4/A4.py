import json
import csv
import math
from collections import Counter

def classify(id, data):
    datalist = data.split()
    probability = [0.0, 0.0, 0.0, 0.0]
    # calc (word|A) (word|B) (word|E) (word|V)
    i = 0
    for classtype in word_count:
        for word in datalist:
            if word in supercount.keys():
                weight = math.log10(4000/supercount[word])
                if word in classtype.keys():
                    probability[i] += math.log10(weight*classtype[word]) + math.log10(class_freq[i]) + math.log10(1/super_dict[word])
            else:
                if word in classtype.keys():
                    probability[i] += math.log10(classtype[word]) + math.log10(class_freq[i]) + math.log10(1/super_dict[word])
        i += 1
    return probability


#log(ab) = log(a) + log(b)
class_freq = [128, 1602, 2144, 216] # fequencey of class a, b, e, v
word_count = [] #a_word_count=0, b_word_count=1 e_word_count=2, v_word_count=3 
with open('Awordcount.json') as file:
    word_count.append(Counter(json.load(file)))
with open('Bwordcount.json') as file:
    word_count.append(Counter(json.load(file)))
with open('Ewordcount.json') as file:
    word_count.append(Counter(json.load(file)))
with open('Vwordcount.json') as file:
    word_count.append(Counter(json.load(file)))

with open('Supercount.json') as file:
    supercount = Counter(json.load(file))

super_dict = Counter()
super_dict = word_count[0] + word_count[1] + word_count[2] + word_count[3]

vocab_size = len(super_dict.keys())
word_count_size = [sum(word_count[0].values()), sum(word_count[1].values()), sum(word_count[2].values()), sum(word_count[3].values())] 


types = ["A", "B", "E", "V"]

with open('tst.csv', 'r') as file:
    file.readline()
    with open('kaggle_submit.csv', 'w', newline='') as kaggle:
        writer = csv.writer(kaggle)
        writer.writerow(["id","class"])
        for line in file:
            dataset = line.split(",")
            dataset[1] = dataset[1][1:-2]
            classification = classify(dataset[0], dataset[1])
            index, value = classification.index(max(classification)), max(classification)     


            print(classification, index, value)
            writer.writerow([dataset[0],types[index]])