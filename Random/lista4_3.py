import random

vet1 = random.sample(range(1, 100), 10)
vet2 = random.sample(range(1, 100), 10)
vet3 = []

for i in range(len(vet1)):
    for v in range(len(vet2)):
        if(vet1[i] == vet2[v]):
            vet3.append(vet1[i])
print(f"Vetor 1: {vet1} \nVetor 2: {vet2} \nVetor 3: {vet3}")
