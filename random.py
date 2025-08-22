import random
guesses_made = 0
number = random.randint(1, 100)

print("Загадано число от 1 до 100")
while guesses_made < 5:
    guess= int(input("Введите ваше предложение: "))
    guesses_made += 1

    if guess < number:
        print("Нужно больше")
    elif guess > number:
        print("Нужно меньше")
    else:
        print("Ты угадал мое число!")
        break
else:
    print("Ты не угадал! Мое число ", number)
