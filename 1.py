import re
with open("D:/words.txt") as f : 
    text = f.read().lower()
regex = re.findall(r'^[^ansepvowdgr]i[^ansepvowdgr]th$',text,re.MULTILINE)

print(regex)


def WordsScore(word):
    freq = 'esiarntolcdugpmkhbyfvwzxqj'
    score = 0 
    for c in word :
        if c in freq:
            score += freq.index(c)
        else: 
            score += 1000
    return word,score
score_list = []
for word in regex:
    if len(word) == len(set(word)) and 'i' in word:
        w,s = WordsScore(word)
        score_list.append((s,w))
score_list.sort()
print(score_list[0])
    