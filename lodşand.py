import random 

ders = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

parola_uzunlugu = int(input("parolanın uzunluğu"))

parola = ""

for i in range(parola_uzunlugu):
    parola += random.choice(ders)

print(f"parola: {parola}")