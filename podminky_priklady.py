vstup = input("Zadej cislo: ")
try:
    cislo = int(vstup)
except:
    cislo = 0

print("vstup = " + vstup)

# napiste program, ktery vypise jednu z nasledujicich vet:
# 1. cislo je mensi nez 10
# 2. cislo je vetsi nez 10 a mensi nez 20
# 3. cislo je vetsi nez 20

if cislo < 10:
    print("cislo je mensi nez 10")
elif cislo < 20:
    print("cislo je vetsi nez 10 a mensi nez 20")
else:
    print("cislo je vetsi nez 20")

# napiste program, ktery vypise vsechny pravdive vety:
# 1. cislo je vetsi nez 10
# 2. cislo je sude
# 3. cislo je liche
# 4. cislo je vetsi nez 10, ale mensi nez 20.

if cislo > 10:
    print("cislo je vetsi nez 10")
if cislo%2 == 0:
    print("cislo je sude")
else:
    print("cislo je liche")
if ((cislo > 10) and (cislo < 20)):  # lze i (20 > cislo > 10)
    print("cislo je vetsi nez 10, ale mensi nez 20.")


if cislo > 10:
    if cislo > 20:
        print("ahoj")
    else:
        print("cau")
    if cislo > 15:
        print("nazder")
    else:
        print("hello")
else:
    if cislo < 10:
        print("privit")
    else:
        print("lalalala")