notas = []
total = 0
media = 0
for i in range (4):
    notas.append(int(input()))
    total = total + notas[i]
media = total/len(notas)
print(f"Notas: {notas}, total: {total}, media: {media}")

