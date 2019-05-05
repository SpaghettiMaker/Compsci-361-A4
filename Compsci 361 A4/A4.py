import json
import csv
import math

def classify(id, data):
    datalist = data.split()
    probability = [0.0, 0.0, 0.0, 0.0]
    # calc (word|A) (word|B) (word|E) (word|V)
    i = 0
    for classtype in word_count:
        for word in datalist:
            if word in classtype.keys():
                probability[i] += math.log10(classtype[word]/word_count_size[i] + 1/vocab_size)

        i += 1
    return probability


#log(ab) = log(a) + log(b)
word_count = [] #a_word_count=0, b_word_count=1 e_word_count=2, v_word_count=3 
with open('Awordcount.json') as file:
    word_count.append(json.load(file))
with open('Bwordcount.json') as file:
    word_count.append(json.load(file))
with open('Ewordcount.json') as file:
    word_count.append(json.load(file))
with open('Vwordcount.json') as file:
    word_count.append(json.load(file))

super_dict = {}
for i in word_count:
    super_dict.update(i)

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
            index, value = classification.index(min(classification)), min(classification)     

            print(classification, index, value)
            writer.writerow([dataset[0],types[index]])