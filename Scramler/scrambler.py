# ---based on 'Oleg Shpagin' code---
import os
from cryptography.fernet import Fernet
from termcolor import colored


# --------------------------------------------------------------------
main_dir = "t:\\Programmes\\SCRIPTS\\Python\\Projects\\Test Cipher\\"   # Here I identified that directory where I want to encrypt my files,
                                                                        # but you always able to change it for yourself
key = Fernet.generate_key()

if not os.path.exists('written_key.txt'):                               # 
    with open('written_key.txt', 'wb') as k:                            # 
        k.write(key)                                                    # This construction works to create/show very important cipher key
else:                                                                   # You must save this key, so that in future decrypt files!
    print(colored('Ключ уже создан.', 'yellow'))                        #
    key = open('written_key.txt', 'rb').read()                          #

print(colored(f'Ваш сгенерированный ключ -- {key}', 'blue'))
cip = Fernet(key)                                                       # Here I had created a main cipher algorithm which is based on our key
# -----------------------------------------------------------------------------------------

if not os.path.isfile('result.txt'):                                  # This's main 'if' construction which checks file availability   
    with os.scandir(path = main_dir) as it:                           # and after that encrypt all files in the main directory
        for entry in it:

            if not entry.is_file():
                print(colored(f'Директория: {entry.name}', 'yellow'))
            else:
                read_file = open(main_dir + entry.name, 'rb').read()
                encrypted = cip.encrypt(read_file)
                with open(main_dir + entry.name, 'wb') as f:
                    f.write(encrypted)
                print(colored(f'Файл зашифрован: {entry.name}', 'green'))

                with open('result.txt', mode = 'w', encoding = 'utf-8') as r:  # Here creation of file "result.txt"(it's a simple log) happens 
                    r.write('Успешно!')
                r.close()
else:                                                                                        # This's main 'else' construction which checks file availability                         
    deal = input(colored('Объект(-ы) уже зашифрован(-ы). Хотите расшифровать -- ', 'red'))   # and after that decrypt all files in the main directory or doing nothing with files

    if deal == 'да':
        with os.scandir(path = main_dir) as it:
            for entry in it:

                if not entry.is_file():
                    print(colored(f'Директория: {entry.name}', 'yellow'))
                else:
                    view_files = open(main_dir + entry.name, 'rb').read()
                    decrypted = cip.decrypt(view_files)
                    with open(main_dir + entry.name, 'wb') as f:
                        f.write(decrypted)
                    print(colored(f'Файл расшифрован: {entry.name}', 'green'))
    else:
        print(colored('Завершение.', 'green'))
# -----------------------------------------------------------------------------------------