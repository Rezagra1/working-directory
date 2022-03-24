freq = 'seiarntolcdugmphbyfkvwzxjq'
with open('E:/words3.txt') as f :
    text = f.readlines()
    text = [x.strip('\n') for x in text]
    score = 0
for word in text :
    if len(word) == 5 : 
        print(word)
           
freq = 'seiarntolcdugmphbyfkvwzxjq'
