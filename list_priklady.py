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

# priklad 3: Zjistěte, kolik prvků v poli je větších než 5.

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

# Vytvořte nové pole, které bude obsahovat prvky v obráceném pořadí.

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
