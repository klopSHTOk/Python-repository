from random import randint


def game():

    def core_hello():

        print('Приветствую, это игра "Угадай число"!')
        name = input('Для начала укажите своё имя: ')

        def core_process():

            print(f'\nИтак, {name}, попробуй угадать некоторое число!')
            exactly = randint(0, 101)
            while True:
                try:
                    number = int(input('Вводи: '))
                    if number == exactly:
                        print('Это великолепная победа!')
                        break

                    elif number < exactly:
                        print(f'Неверно, заданное число больше введённого на {exactly - number}!')
                        continue

                    elif number > exactly:
                        print(f'Неверно, искомое число меньше введённого на {number - exactly}!')
                        continue

                except ValueError:
                        choice = input(('Ты ввёл букву!\nХочешь продолжить? '))
                        if choice == "Да":
                            print('Ок, пробуй ещё.')
                            continue
                        else:
                            print('Хорошо, завершаем.\nСпасибо за игру!')
                            break
        core_process()

    core_hello()
    
game()        