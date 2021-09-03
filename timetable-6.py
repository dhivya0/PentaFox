import random
days=["Monday","Tuesday","Wednesday","Thursday","Friday"]
hr=["1","2","3","4","5"]
subject=["Python","English","Maths","Chemistry","Physics"]
print("\t\t"+hr[0]+"\t\t"+hr[1]+"\t\t"+hr[2]+"\t\t"+hr[3]+"\t\t"+hr[4])
for i in range(0,5):
    print(days[i],end="    \t")
    print(subject[random.randrange(0,5)],end="\t    ")
    print(subject[random.randrange(0,5)],end="\t    ")
    print(subject[random.randrange(0,5)],end="\t    ")
    print(subject[random.randrange(0,5)],end="\t    ")
    print(subject[random.randrange(0,5)],end="\t    ")
    print()
