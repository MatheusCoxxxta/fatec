word = str(input())

drow = word[::-1]

if(drow != word):
    print("Não palindrome")
else:
    print("Palindrome")

