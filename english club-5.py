def compare(name1,name2):
    result=""
    for i in range(len(name1)):
        if name1[i] in name2:
            continue
        else:
            result=result+name1[i]
    return result

name1=input()
name2=input()
res1=compare(name1,name2)
res2=compare(name2,name1)
print(res1+res2)
