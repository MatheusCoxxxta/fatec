def python(p):
    for c in p:
        if c in 'python':
            return True
    return False

text = '''The Python Software Foundation and the global Python
community welcome and encourage participation by everyone. Our community is based on
mutual respect, tolerance, and encouragement, and we are working to help each other live up
to these principles. We want our community to be more diverse: whoever you are, and
whatever your background, we welcome you'''

text = text.replace('.', '')
text = text.replace(',', '')
text = text.replace(':', '')
text = text.lower()

words = text.split()

cont = 0

for p in words:
    if len(p) > 4 and python(p):
        cont = cont + 1
print(cont)

