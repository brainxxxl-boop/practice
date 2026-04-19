import random

def play_game():
    print("--- ИНСТРУКЦИЯ: Угадайте число от 1 до 100 ---")
    print("Команды: введите число или 'выход' для завершения.")
    
    target = random.randint(1, 100)
    attempts = 0
    max_attempts = 10  # Лимит для пользовательского опыта

    while attempts < max_attempts:
        user_input = input(f"Попытка {attempts + 1}/{max_attempts}. Ваш вариант: ")
        
        if user_input.lower() == 'выход':
            return False

        try:
            guess = int(user_input)
            
            # Валидация диапазона
            if not (1 <= guess <= 100):
                print("Ошибка: число должно быть от 1 до 100!")
                continue
                
            attempts += 1
            
            if guess < target:
                print("Слишком маленькое.")
            elif guess > target:
                print("Слишком большое.")
            else:
                print(f"Поздравляю, вы угадали! Число: {target}. Попыток: {attempts}")
                return True

            # Игровая логика: подсказка после 5 попыток
            if attempts == 5:
                low = max(1, target - 10)
                high = min(100, target + 10)
                print(f"ПОДСКАЗКА: Число находится между {low} и {high}")

        except ValueError:
            print("Ошибка: введите целое число.")

    print(f"Попытки закончились. Было загадано: {target}")
    return True

if __name__ == "__main__":
    while True:
        if not play_game():
            break
        if input("Сыграть еще раз? (да/нет): ").lower() != 'да':
            break
