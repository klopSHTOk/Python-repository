import os                      # os - to work with the directories;
import time                    # time - to make delays between code parts;
from termcolor import colored  # # termcolor - to color some sentences


# ---------------------------------------------------------------------------------
print('~' * 80)                                 # This thing I'll use for all code length to do sections
print(colored('Добро пожаловать!', 'green'))

offer = colored('Выберите то, что хотите видеть на странице сервера...', 'yellow')     
for o in offer:                                 # By this construction I made symbol by symbol string output
    print(o, end='', flush=True)
    time.sleep(0.1)

time.sleep(1)
print('\n')
print('~' * 80)

def func_to_choose(*abilities):

    """This function uses to output user abilities in the HTML - script.

    It's very important to make him/her own page."""

    sign = (colored('[*]', 'yellow'))

    num = 1
    for ability in abilities:
        print('\n')
        print(f'\t{sign} {num} -- {ability}')
        print('\n')
        num += 1

func_to_choose('Текст', 'Текст со ссылкой', 'Изображение')
time.sleep(1)
print('~' * 80)

choose = int(input('Ваш выбор -- '))
# ---------------------------------------------------------------------------------

if choose == 1:     # Here the user choses number one to add some words on his/her own page
    print('\n')
    print('-' * 80)

    def text():

        """This function writes a sentence with user parameters, such as title and tag.
        
        I'll use these things in whole my code."""

        print(colored('Отлично!', 'green'))
        print('\n')

        title = input('\tУкажите название вашей страницы -- ')
        words = input('\tА теперь укажите текст для страницы -- ')
        tag = input('\tНаконец, укажите тег для текста(h1, strong, em) -- ')

        cgi_dir = 't:\\Programmes\\SCRIPTS\\GitHab\\pyrepository\\Server\\web\\cgi\\'         # Here we change current directory to add HTML-script in a new one
        os.chdir(cgi_dir)
        with open('script.html', mode='w', encoding='utf-8') as s:
            s.write('<!DOCTYPE html>\n'
                    '<html>\n'
                    '<head>\n'
                    '\t<meta charset="UTF-8">\n'
                    f'\t<title>{title}</title>\n'
                    '</head>\n'
                    '<body>\n'
                    f'\t<{tag}>{words}</{tag}>\n'
                    '</body>\n'
                    '</html>')
            s.close()
        print('\n')

        time.sleep(1)
        address = colored('http://localhost:8000/', 'yellow')
        all_great = colored('Страничка создана по вашему желанию', 'green')
        server_here = f'Перейдите по ссылке во вкладку "cgi/script.html":\n\t{address}'   # Here users can go over to their own server

        print(all_great)
        print(server_here)
        print('-' * 80)
        print('\n')

    text()
# ---------------------------------------------------------------------------------

elif choose == 2:
    print('\n')
    print('-' * 80)

    def text_with_link():

        """This function writes sentence with a link"""

        print(colored('Весьма хорошее решение.', 'green'))
        print('\n')

        title = input('\tУкажите название вашей страницы -- ')
        words = input('\tТеперь укажите текст для страницы -- ')
        link = input('\tПропишите нужную ссылку -- ')

        cgi_dir = 't:\\Programmes\\SCRIPTS\\GitHab\\pyrepository\\Server\\web\\cgi\\'
        os.chdir(cgi_dir)
        with open('script.html', mode='w', encoding='utf-8') as s:
            s.write('<!DOCTYPE html>\n'
                    '<html>\n'
                    '<head>\n'
                    '\t<meta charset="UTF-8">\n'
                    f'\t<title>{title}</title>\n'
                    '</head>\n'
                    '<body>\n'
                    f"\t<a href='{link}', target='_blank'>{words}</a>\n"
                    '</body>\n'
                    '</html>')
            s.close()
        print('\n')

        time.sleep(1)
        address = colored('http://localhost:8000/', 'yellow')
        all_great = colored('Страничка создана по вашему желанию', 'green')
        server_here = f'Перейдите по ссылке во вкладку "cgi/script.html":\n\t{address}'

        print(all_great)
        print(server_here)
        print('-' * 80)
        print('\n')

    text_with_link()
# ---------------------------------------------------------------------------------

else:
    print('\n')
    print('-' * 80)

    def image(): 

        """And the last one function creates a page with some image which user can add"""

        print(colored('Хорошая мысль!\nДобавтье изображение в директорию t:\\Programmes\\SCRIPTS\\GitHab\\pyrepository\\Server\\web\\cgi\\images', 'green'))
        print('\n')  

        title = input('\tУкажите название вашей страницы -- ')
        picture = input('\tУкажите название изображения -- ')

        cgi_dir = 't:\\Programmes\\SCRIPTS\\GitHab\\pyrepository\\Server\\web\\cgi\\'
        os.chdir(cgi_dir)
        with open('script.html', mode='w', encoding='utf-8') as s:
            s.write('<!DOCTYPE html>\n'
                    '<html>\n'
                    '<head>\n'
                    '\t<meta charset="UTF-8">\n'
                    f'\t<title>{title}</title>\n'
                    '</head>\n'
                    '<body>\n'
                    f"\t<img src='images/{picture}'>\n"
                    '</body>\n'
                    '</html>')
            s.close()
        print('\n')


        time.sleep(1)
        address = colored('http://localhost:8000/', 'yellow')
        all_great = colored('Страничка создана по вашему желанию', 'green')
        server_here = f'Перейдите по ссылке во вкладку "cgi/script.html":\n\t{address}'

        print(all_great)
        print(server_here)
        print('-' * 80)
        print('\n')

    image()
# ---------------------------------------------------------------------------------