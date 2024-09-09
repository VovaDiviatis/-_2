import random
simvol = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
dlina = int(input("введите длину пароля"))
new_simvol = ""
for i in range(dlina):
    new_simvol += random.choice(simvol)
print(new_simvol)