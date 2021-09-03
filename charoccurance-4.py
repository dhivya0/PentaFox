def check(word):
    new=word
    for i in range(len(word)):
        count=word.count(word[i])
        if count>=2:
            occur=word.find(word[i])
            new=word[:occur+1]+str(count)+word[occur+count:]
    print(new,end=" ")

text=list(map(str,input().split()))
for i in range(len(text)):
    check(text[i])
