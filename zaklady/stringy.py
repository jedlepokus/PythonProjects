text = "ahoj"
text2 = 'ahooj'
text3 = "Sean O'Connery"
text4 = 'tak rekl: "to je ale ..." A tim to skoncilo.'
text5 = 'Sean O\'Connery'
text6 = " cesta k souboru je c:\\hry\\soubor.txt"
text7 = "ahoj \\n nazdar"
print(text5)
print(text6)
print(text7)

a = "ahoj"
b = "pane"

print(a+b)
print(a*3)

c = "a"
for i in range(5):
    c = c + "a"

print(c)

promenna = "Ahoj Karle, jak se máš?"
print(promenna[6])  # indexovani od 0 !!!
print(len(promenna))
for i in range(len(promenna)):
    print(promenna[i])
print(promenna[len(promenna)-1])
print(promenna[-1])
print(promenna[5:10:2])
print(promenna[10:5:-2])
print(promenna[5:])
print(promenna[:5])
print(promenna[:5:-1])
print(promenna[::-1])
print(promenna.index(","))