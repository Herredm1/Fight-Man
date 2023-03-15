import random

names = []

fileName = r'names.txt'

with open(fileName,'r') as f_object:
    word_lst = f_object.read().split()

num = 30    
while num > 0:
    word = random.choice(word_lst)
    if word in names:
        continue
    else:  
        names.append(word)
        num -= 1
    
print(names)
    