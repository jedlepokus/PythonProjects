def secti(a, b):
    return a+b  # vraci cislo

def vypis_soucet(a, b):
    print(a+b)  # vraci "None" <- nic nevraci

def vypis_print_soucet(a, b):
    return print(a+b)  # vraci "None" fce  print() vraci None

print(secti(2,3))
print("********")
print(vypis_soucet(2,3))
print("********")
print(vypis_print_soucet(2,3))
