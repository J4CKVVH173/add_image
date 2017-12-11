from django.shortcuts import render
from django.http import HttpResponse
import os
from django.views import View

from mainApp.forms import NameForm
from mainApp.models import Files_from_client

# Create your views here.
def index(request):
#Функция рендерящая шаблон html и докидывающая туда формы
    form = NameForm()
    return render(request, 'index.html', {'form': form})

def handle_uploaded_file(f, name):
#Обработчи принятого файла, построчно перезаписывает файл построчно по указанному пути
    #Сохранение пути до корневой папки проекта
    path = os.getcwd()
    #Создание директории с именем полученым от клиента
    os.mkdir(r"{0}\media\{1}".format(path, name), mode=0o777)
    #Завись файла в созданый директорий
    with open('media/{0}/{1}'.format(name, f), 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

class Test(View):
    def get(self, request):
        return HttpResponse("Hello word")

    def post(self, request):
        #Проверка правильности входящего метода

            #Создание двух переменныех, первая принимает все input сообщения кроме
            #files и images
            infor = request.POST
            #Прием files or images

            infor_file = request.FILES
            len_files = request.FILES.__len__()
            #Создание переменное, как новый элемент бд
            # new_bd = Files_from_client(name=infor['your_name'], file=infor_file['file'])
            # #СОхранение нового поля в бд
            # new_bd.save()
            # #Передача принятого файла в обработчик для перезаписи в текстовик
            handle_uploaded_file(request.FILES['file'], infor['your_name'])

            return render(request, 'test.html')
