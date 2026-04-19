import random

# Загадываем число один раз при запуске
secret = random.randint(1, 100)

print("--- ИГРА НАЧАЛАСЬ ---")
print("Я загадал число от 1 до 100. У тебя 10 попыток.")

popitka = 1
while popitka <= 10:
    try:
        # Спрашиваем число у игрока
        vvod = input(f"Попытка {popitka}/10. Введи число и нажми Enter: ")
        
        # Превращаем текст в число
        nomer = int(vvod)
        
        # Сравниваем
        if nomer < secret:
            print("ОТВЕТ: Мало! Моё число БОЛЬШЕ.")
        elif nomer > secret:
            print("ОТВЕТ: Много! Моё число МЕНЬШЕ.")
        else:
            print(f"ПОБЕДА! Ты угадал за {popitka} попыток!")
            break
            
        # Даем подсказку на 5-й попытке
        if popitka == 5:
            print(f"Подсказка: число где-то между {secret-5} и {secret+5}")
            
        popitka += 1
        
    except ValueError:
        print("ОШИБКА: Нужно вводить только цифры!")

if popitka > 10:
    print(f"ПОПЫТКИ КОНЧИЛИСЬ. Было загадано: {secret}")

input("Нажми Enter, чтобы закрыть окно...")
