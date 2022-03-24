import re
with open('E:\words2.txt') as f :
    text = f.read()
    d = {}
    for i in 'abcdefghijklmnopqrstuvwxyz':
        n =text.count(i)
        d.setdefault(i,n)
key =[]
value = []
for k,v in d.items() :
    key.append(k)
    value.append(v)
value.sort()
value.reverse()
for i in range(32):
    for k , v in d.items():
        if v == value[i]:
            print(k)
            
