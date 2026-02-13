import numpy as np

limit_dolni = 0
limit_horni = 20
target = np.random.randint(limit_dolni, limit_horni + 1)
attempts = 0

while True:
    while True:
        guess_text = input("Hadej cislo od 0 do 20 (vcetne): ")
        try:
            guess = int(guess_text)
            break
        except:
            print("neni cislo")
    attempts += 1
    if guess > target:
        print("hadas moc vysoko")
    elif guess < target:
        print("hadas moc nizko")
    else:
        print("spravne - pocet pokusu: " + str(attempts))
        break
