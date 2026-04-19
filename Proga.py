
import random

def start_game():
    target = random.randint(1, 100)
    print("--- ИГРА: УГАДАЙ ЧИСЛО (1-100) ---")
    print("У тебя есть 10 попыток.")
    
    attempts = 0
    while attempts < 10:
        attempts += 1
        try:
            # Запрашиваем число
            guess = int(input(f"Попытка {attempts}/10. Введи число: "))
            
            # Самая важная часть: сравнение
            if guess < target:
                print("МАЛО! Загаданное число БОЛЬШЕ.")
            elif guess > target:
                print("МНОГО! Загаданное число МЕНЬШЕ.")
            else:
                print(f"КРАСАВА! Угадал за {attempts} попыток!")
                return # Выходим из функции, так как победили

            # Подсказка на 5-й попытке (как в задании)
            if attempts == 5:
                print(f"--- ПОДСКАЗКА: Число где-то рядом с {target + random.randint(-5, 5)} ---")

        except ValueError:
            print("Ошибка! Нужно вводить именно ЦИФРЫ.")
            attempts -= 1 # Не считаем попытку, если ввели ерунду

    print(f"Попытки кончились! Я загадал число {target}.")

if __name__ == "__main__":
    start_game()
    input("\nНажми Enter, чтобы выйти...")
