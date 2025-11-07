promenna = "Ahoj Karle, jak se máš?"

# vypište jednotlive znaky pod sebe
# (pomoci for-cyklu)

for i in range(len(promenna)):
    print(promenna[i])

# totez, ale pozpatku...

for i in range(len(promenna)):
    print(promenna[-i-1])

for i in range(len(promenna)-1, -1, -1):
    print(promenna[i])

# vzpis pyramidu znaku:
print("****")
for i in range(len(promenna)):
    print(promenna[:i+1])


print("****")
for i in range(len(promenna)-2):
    print(promenna[i:i+3])

# vypiste vedle sebe vzdy prvni a posledni pismenko,
# pak, druhy a predposledni, ... koncime v polovine textu

print(int(5.9))

for i in range(int(len(promenna)/2)+1):
    print(promenna[i], promenna[-i-1])

#promenna = promenna.replace("a", "X")
print(promenna)
print(promenna.strip())
a = "       lwefwefnwef "
print(a)
print(a.strip())
a = "5"

print(a.zfill(5))