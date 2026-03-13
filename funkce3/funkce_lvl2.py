def moje_funkce(a, b, c):
    return a+b+c

print(moje_funkce(2,3,4))

def jina_funkce(a, b, c=100, d=10):
    return a+b+c+d

print(jina_funkce(1,2))
print(jina_funkce(1,2,3))
print(jina_funkce(1,2,3,4))
print(jina_funkce(1,2, d=5))
print(jina_funkce(b=1, c=2, d=5, a=10))

def jeste_jina_funkce(*args):
    print(args)
    soucet = 0
    for i in range(len(args)):
        soucet +=args[i]
    return soucet

print(jeste_jina_funkce(1,2,3,4))
print(jeste_jina_funkce(1,2))
print(jeste_jina_funkce(1,2,3,4,5,6,7,8))
