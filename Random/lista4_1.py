import random

num = []
maior = 0
num = random.sample(range(1, 100), 10)

for i in range(len(num)):
    if(num[i] > maior):
        maior = num[i]
    else:
        maior = maior
print(num)
print(maior)
