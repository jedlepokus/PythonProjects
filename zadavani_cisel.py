while True:
    cislo_jako_text = input("Zadej cislo: ")
    try:
        cislo = int(cislo_jako_text)
        break
    except:
        print("neni platne cislo")

print("zadane cislo + 10 = " + str(cislo + 10))