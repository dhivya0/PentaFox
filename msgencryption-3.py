import random
message=input()
prefix=random.choice(message)
print(prefix.upper()+message[::-1])
