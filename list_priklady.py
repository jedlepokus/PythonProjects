# priklad 1: najdete maximalni prvek v listu a jeho pozici

pole = [5, 2, 9, 1, 7, 3, 10, 6, 4]

maximalni_prvek = pole[0]  # nastavim dosavadni nalezene maximum podle 0. prvku pole.
pozice_max_prvku = 0  # nastavim pozici maximalniho prvku na index 0.

for i in range(1, len(pole)):  # 0. prvek je jiz nastaven - zacnu tedy od 1. (ale kdyz necham nulu, nic se nestane)
  if maximalni_prvek < pole[i]:  # pokud je i-ty prvek vetsi nez dosavadni maximum...
    maximalni_prvek = pole[i]  # ... nastavim maximum na i-ty prvek
    pozice_max_prvku = i  # ... a pozici nejvetsiho prvku na i

print("{} je maximalni prvek a je na pozici {}".format(maximalni_prvek, pozice_max_prvku))  # vypis vysledku

# priklad 2: Napište program, který najde nejmenší prvek v poli.

pole = [5, 2, 9, 1, 7, 3, 1, 6, 4]

minimalni_prvek = pole[0]  # nastavim dosavadni nalezene minimum podle 0. prvku pole.
pozice_min_prvku = 0  # nastavim pozici minimalniho prvku na index 0.

for i in range(1, len(pole)):  # 0. prvek je jiz nastaven - zacnu tedy od 1. (ale kdyz necham nulu, nic se nestane)
  if minimalni_prvek > pole[i]:  # pokud je i-ty prvek vetsi nez dosavadni maximum...
    minimalni_prvek = pole[i]  # ... nastavim maximum na i-ty prvek
    pozice_min_prvku = i  # ... a pozici nejvetsiho prvku na i

print("{} je minimalni prvek a je na pozici {}".format(minimalni_prvek, pozice_min_prvku))  # vypis vysledku

# priklad 3: Vypočítejte průměrnou hodnotu všech prvků v poli.

pole = [5, 2, 9, 1, 7, 3, 1, 6, 4]

soucet = 0

for i in range(len(pole)):
    soucet = soucet + pole[i]
    # soucet += pole[i]  # tohle je to same jako o radek vys

print(soucet/len(pole))

# priklad 4: Zjistěte, kolik prvků v poli je větších než 5.

pole = [5, 2, 9, 1, 7, 3, 10, 6, 4]

pocitadlo = 0
limit = 5

for i in range(len(pole)):
    if pole[i] > limit:
        pocitadlo += 1

print("Pocet prvku vetsich nez "+str(limit)+" je: " + str(pocitadlo))


# priklad 5: Spočítejte součet všech hodnot v poli.

pole = [5, 2, 9, 1, 7, 3, 1, 6, 4]

soucet = 0

for i in range(len(pole)):
    soucet = soucet + pole[i]
    # soucet += pole[i]  # tohle je to same jako o radek vys

print("soucet prvku v listu je " + str(soucet))

# příklad 7: Vytvořte nové pole, které bude obsahovat prvky v obráceném pořadí.

pole = [5, 2, 9, 1, 7, 3, 1, 6, 4]
nove_pole = []

for i in range(len(pole)-1, -1, -1):
    nove_pole.append(pole[i])

print(nove_pole)


nove_pole = []

for i in range(len(pole)):
    nove_pole.append(pole[-i-1])

print(nove_pole)
nove_pole = []

nove_pole = pole[::-1]

print(nove_pole)

# priklad 8: dve pole se stejnzm pocetem prvku, secist prvek po prvku
pole = [5, 2, 9, 1, 7, 3, 10, 6, 4]
pole2 = [3, 5, 4, 7, 5, 3, 4, 5, 10]
pole_vysledne = []

for i in range(len(pole)):
  pole_vysledne.append(pole[i] + pole2[i])

print(pole_vysledne)




# priklad 8.5: pole sectete v opacnem poradi (0 - last, 1 - last-1, ...)
pole_vysledne = []
for i in range(len(pole)):
  pole_vysledne.append(pole[i] + pole2[-i-1])

print(pole_vysledne)

# prikald 9: najdete druhy nejvetsi prvek v poli

pole = [15, 7, 13, 4, 12, 10, 14, 11, 7]
max = -1000
druhy = -1000
# alternativni incializace:
if len(pole) >= 2:
    if pole[0] > pole[1]:
        max = pole[0]
        druhy = pole[1]
    else:
        max = pole[1]
        druhy = pole[0]
# for i in range(2, len(pole))

for i in range(len(pole)):
    if pole[i] > max:
        druhy = max
        max = pole[i]
    elif pole[i] > druhy:
        druhy = pole[i]

print(max)
print(druhy)

# prikald 10: zjistete zda je pole serazene
pole = [15, 7, 13, 4, 12, 10, 14, 11, 7]
je = True
for i in range(len(pole)-1):
    if pole[i] > pole[i+1]:
        je = False
        break
if je:
    print("je")
else:
    print("neni")


# priklad bonus:

sude = 0
liche = 0
for i in range(len(pole)):
    if pole[i] % 2 == 0:
        sude += 1
    else:
        liche +=1

print(sude)
print(liche)

