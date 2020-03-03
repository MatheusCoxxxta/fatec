import random

num = random.sample(range(1, 100), 20)
impar = []
par = []
for i in range(len(num)):
    if(num[i] % 2==0):
        par.append(num[i])
    else:
        impar.append(num[i])
print(f"Numeros: {num} \nPares: {par} \nImpares: {impar}")
