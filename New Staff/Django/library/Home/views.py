from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('<!DOCTYPE html>\n'
                        '<html>\n'
                            '<head>\n'
	                            '<meta charset="UTF-8">\n'
	                            '<title>Главная страница</title>\n'
                            '</head>\n'
                            '<body>\n'
	                            '<h1>Наш фитнес-клуб:</h1>\n'
	                            '<h3>У нас вы можете нанять инструктора, который составит индивидуальную программу оздоровления и укрепления организма.</h3>\n'
	                            '<h3>Также, мы предоставляем услуги массажа, салона красоты, бани, сауны и хаммама.</h3>\n'

	                            '<h1>Про хаммам:</h1>\n'
	                                '<a href="https://m-strana.ru/articles/chto-takoe-khamam/" target="_blank">Если вы не знаете о хаммаме, можете прочитать о нём более подробно.</a>\n'

	                            '<img src="fitness.jpg">\n'
                            '</body>\n'
                        '</html>')