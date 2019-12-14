f = open('families.txt', 'r+', encoding="utf8")
text = f.read()

text.replace(" ", "\n")
f.write(text)

