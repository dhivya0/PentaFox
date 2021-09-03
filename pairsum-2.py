li=list(map(int,input().split()))
s=int(input())
pair=[]
for i in range(len(li)):
    for j in range(i+1,len(li)):
        if li[i]+li[j]==s:
            pair.append(li[i])
            pair.append(li[j])
if len(pair)>0:
    print(*pair)
else:
    print("No pairs found")
