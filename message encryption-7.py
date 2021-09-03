alp=list(map(int,input("Enter the numbers 1-26 with seperated by space").split()))
for i in range(len(alp)):
    print(chr(64+alp[i]))
