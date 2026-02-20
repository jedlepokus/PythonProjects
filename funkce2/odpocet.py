def odpocet(n):
    if n <= 0:
        print("bum")
        return
    else:
        print("Odpocet T-" + str(n))
        odpocet(n-1)

odpocet(7)