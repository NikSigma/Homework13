import random

secret_number = random.randint(1, 100)

print("Вгадай число або помри!")

while True:
    guess = int(input("Спробуй: "))

    if guess < secret_number:
        print("Занадто мале!")
    elif guess > secret_number:
        print("Занадто велике!")
    else:
        print("Вітаю! Ти уникнув смерті😈!")
        break
