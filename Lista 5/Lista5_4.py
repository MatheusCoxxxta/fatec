#Questão D. Daniela é uma pessoa muito supersticiosa. Para ela, um número é sortudo
#se ele contém o dígito 2 mas não o dígito 7. Então, na opinião dela, quantos números
#sortudos existem entre 18644 e 33087, incluindo os extremos?
count = 0
for i in range(18643, 33088):
    if '7' not in str(i) and '2' in str(i):
        count += 1
print(count)