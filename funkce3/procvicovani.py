import numpy as np

# napiste funkci:
# 1. ktera vrati 2. nejvetsi cislo v seznamu
#       - vstup: list
#       - vystup: cislo (hodnota 2. nejvyssiho cisla

def druhe_nej(vstup_list):
    if vstup_list[0] > vstup_list[1]:
        maxim = vstup_list[0]
        druhe = vstup_list[1]
    else:
        maxim = vstup_list[1]
        druhe = vstup_list[0]

    for i in range(2, len(vstup_list)):
        if vstup_list[i] > maxim:
            druhe = maxim
            maxim = vstup_list[i]
        elif vstup_list[i] > druhe:
            druhe = vstup_list[i]
    return druhe

l = [50, -5, 20, -6, 15, 26, 23, 15]
print(druhe_nej(l))

# 2. funkce zjisti, jestli je cislo prvocislo
#       - vstup : cislo
#       - vystup : logicka promenna (True/False)

def je_prvocislo(n):
    if n < 2:
        return False
    #for i in range(2, int(n**(1/2)+1)):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

print(je_prvocislo(12))
print(je_prvocislo(7))
print(je_prvocislo(2))
#print(je_prvocislo(int(input("zadej cislo"))))



# 3. funkce, ktera spocita prvocisla v seznamu
#       - vstup: list (seznam celych cisel)
#       - vystup: cislo (pocet prvocisel)



def pocet_prvocisel(seznam_cisel):
    pocitadlo = 0
    for cislo in seznam_cisel:
        if je_prvocislo(cislo):
            pocitadlo += 1
    return pocitadlo

def pocet_prvocisel2(seznam_cisel):
    pocitadlo = 0
    for i in range(len(seznam_cisel)):
        if je_prvocislo(seznam_cisel[i]):
            pocitadlo += 1
    return pocitadlo

muj_seznam = [5, 13, 31, 55, 17, 54]
print(pocet_prvocisel(muj_seznam))






def adding(a, b):
    return a + b

def subtracting(c, d):
    return c - d

def calculate(funkce, x, y):
    return funkce(x, y)

print("*******************")
print(calculate(adding, 2, 3))
print(calculate(subtracting, 2, 3))

pejsek = int(input("zdej cislo: "))
kocicka = int(input("zadej druhy cislo: "))
ptacek = input("zadej funkci (+/-)")

if ptacek == "+":
    print(calculate(adding, pejsek, kocicka))
elif ptacek == "-":
    print(calculate(subtracting, pejsek, kocicka))
else:
    print("neznama funkce")

