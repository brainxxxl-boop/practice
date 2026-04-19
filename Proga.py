import random

# Загадываем число
secret_number = random.randint(1, 100)

print("=== ИГРА ЗАПУЩЕНА ===")
print("Я выбрал число от 1 до 100.")

for i in range(1, 11):
    # Добавляем явный текст перед вводом
    user_input = input(f"\n[ШАГ {i}] Введите ваше число: ")
    
    try:
        guess = int(user_input)
        
        # Сразу печатаем результат сравнения
        if guess < secret_number:
            print(f"--- РЕЗУЛЬТАТ: {guess} - это МАЛО! (Нужно больше) ---")
        elif guess > secret_number:
            print(f"--- РЕЗУЛЬТАТ: {guess} - это МНОГО! (Нужно меньше) ---")
        else:
            print(f"!!! ПОЗДРАВЛЯЮ !!! Ты угадал число {secret_number}!")
            break
            
        # Подсказка на 5-й попытке (по заданию)
        if i == 5:
            print(f"ПОДСКАЗКА: Число находится между {secret_number - 7} и {secret_number + 7}")

    except ValueError:
        print("ОШИБКА: Ты ввел не число! Попробуй еще раз.")

print("\nКонец игры. Спасибо за участие!")
