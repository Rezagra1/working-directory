with open("D:\words.txt") as f :
    words = f.readlines()
words = [x.lower() for x in words]
for word in words :
    if len(word) ==  6 and \
        word[0]== 't' and\
        'r' not in word and\
        'i' not in word and\
        'c' not in word and \
        'k' not in word and \
        'w' not in word and\
        'a' not in word and\
        'n' not in word and \
        'o' not in word and \
        'y' not in word and \
        'd' not in word and \
        word[2] == 'e':
        
        
            print(word)
