# for i in range(0, 4):
#     print(i*2)
#     print("ahoj")


# #vypis suda cisla od 0 do 10 vcetne 0 a vcetne 10
# for i in range(0, 11, 2):
#     print(i)
#
# for i in range(6):
#     print(i*2)

# for i in range(0, 11):
#     if i%2==0:
#         print(i)
#
# for i in range(5):
#     for j in range(5):
#         print(str(i) + ", " + str(j))






for i in range(10):
    print(i)
    if i > 5:
        break
    print("ahoj")


while True:
    x = input("napis cislo: ")
    try:
        a = int(x)
        break
    except:
        pass
print(a)