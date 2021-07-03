# Импорт модулей
import random
import sys
import time

# Guesser 0.2 by Planeptunia

# Стартовые переменные и константы
MIN_NUMBER_EASY = 1
MAX_NUMBER_EASY = 75
MAX_ATTEMPTS_EASY = 20
MIN_NUMBER_MED = 1
MAX_NUMBER_MED = 150
MAX_ATTEMPTS_MED = 15
MIN_NUMBER_HARD = 1
MAX_NUMBER_HARD = 250
MAX_ATTEMPTS_HARD = 10
MAX_ATTEMPTS_HARDCORE = 5
MIN_NUMBER_HARDCORE = 1
MAX_NUMBER_HARDCORE = 500
rolls = 0
game_started = False
game_ended = False
hardcore = False
easy = False
medium = False
hard = False
# Проверка на то, начата ли игра и вопрос на игру с хардкором
while game_started == False:
    print('Включить хардкор? (да или нет)')
    hardcore_game = input().lower()
    if hardcore_game == 'да' or hardcore_game == 'д':
        print('Вы уверены?')
        hardcore_sure = input().lower()
        if hardcore_sure == 'да' or hardcore_sure == 'д':
            hardcore = True
        else:
            hardcore = False
    else:
        hardcore = False
    # Выбор сложности
    if hardcore == False:
        print('Выберите сложность (1 - Легкий, 2 - Средний, 3 - Сложный)')
        difficulty = input()
        if int(difficulty) == 1:
            easy = True
            secret_number = random.randint(MIN_NUMBER_EASY, MAX_NUMBER_EASY)
        elif int(difficulty) == 2:
            medium = True
            secret_number = random.randint(MIN_NUMBER_MED, MAX_NUMBER_MED)
        elif int(difficulty) == 3:
            hard = True
            secret_number = random.randint(MIN_NUMBER_HARD, MAX_NUMBER_HARD)
    attempts = 0
    game_started = True
# Цикл попыток
while game_started == True:
    # Включен ли хардкор
    if hardcore == True:
        secret_number = random.randint(MIN_NUMBER_HARDCORE, MAX_NUMBER_HARDCORE)
        rolls += 1
    # ИИ бота и его хардкор версии
    if hardcore == True:
        bot_mode = random.randint(1, 100)
    else:
        bot_mode = random.randint(1, 250) # Определение режима бота
    # Проверка на хардкор
    if hardcore == False:
        if bot_mode <= 25:
            bot_answer = secret_number
        else:
            if easy == True:
                bot_answer = random.randint(MIN_NUMBER_EASY, MAX_NUMBER_EASY)
            elif medium == True:
                bot_answer = random.randint(MIN_NUMBER_MED, MAX_NUMBER_MED)
            elif hard == True:
                bot_answer = random.randint(MIN_NUMBER_HARD, MAX_NUMBER_HARD)
    if hardcore == True:
        if bot_mode <= 30:
            bot_answer = secret_number
        else:
            bot_answer = random.randint(MIN_NUMBER_HARDCORE, MAX_NUMBER_HARDCORE)
    # Вопрос игроку
    print('число?')
    answer = input()
    # Проверка на победу игрока
    if int(answer) == secret_number:
        if hardcore == False:
            print('победа число было %s' % (secret_number))
        elif hardcore == True:
            print('поздравляю с прохождением хардкора')
            print('победа число было %s, число было сменено %s раз' % (secret_number, rolls))
        time.sleep(3)
        game_started = False
        game_ended = True
        break
    # Если ответ игрока больше секретного числа
    elif int(answer) > secret_number:
        attempts += 1
        if hardcore == False:
            print('слишком много')
    # Если ответ игрока меньше секретного числа
    elif int(answer) < secret_number:
        attempts += 1
        if hardcore == False:
            print('слишком мало')
    # Указание на то какое число сказал бот
    print('бот сказал число %s' % (bot_answer))
    # Проверка на победу бота
    if bot_answer == secret_number:
        if hardcore == False:
            print('бот победил правильное число было %s' % (secret_number))
        elif hardcore == True:
            print('бот победил правильное число было %s, число было сменено %s раз' % (secret_number, rolls))
        time.sleep(3)
        game_started = False
        game_ended = True
        break
    # Проверка на проигрыш в хардкоре
    if hardcore == True:
        if attempts > MAX_ATTEMPTS_HARDCORE:
            print('проигрыш правильное число было %s, число было сменено %s раз' % (secret_number, rolls))
            time.sleep(3)
            game_started = False
            game_ended = True
            break
    # Проверка на то, кончились ли попытки у игрока
    if easy == True:
        if attempts > MAX_ATTEMPTS_EASY:
            print('проигрыш правильное число было %s' % (secret_number))
            time.sleep(3)
            game_started = False
            game_ended = True
            break
    if medium == True:
        if attempts > MAX_ATTEMPTS_MED:
            print('проигрыш правильное число было %s' % (secret_number))
            time.sleep(3)
            game_started = False
            game_ended = True
            break
    if hard == True:
        if attempts > MAX_ATTEMPTS_HARD:
            print('проигрыш правильное число было %s' % (secret_number))
            time.sleep(3)
            game_started = False
            game_ended = True
            break
# Конец игры
if game_ended == True:
    if hardcore == False:
        print('Спасибо за игру')
        time.sleep(3)
        sys.exit
