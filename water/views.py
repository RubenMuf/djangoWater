from django.shortcuts import render
from djangoWater.creat_form import Creat_form

# Create your views here.
def home(request):
    return render(request, 'home_form.html')

def socsety(request):
    print(1)
    if request.method == 'POST':
        print(2)
        anketa = Creat_form(request.POST) # через параметр request.POST формируем анкету для дальнейшей проверки
        if anketa.is_valid(): # это значит что анкета составлена без ошибок
            print(3)
            name = request.POST.get('name')
            lastname = request.POST.get('lastname')
            E_mail = request.POST.get('E_mail')
            tel = request.POST.get('tel')
            address = request.POST.get('address')
            month = request.POST.get('month')
            v = request.POST.get('v')
            quantity = request.POST.get('quantity')
            if int(v) == 5:
                price = int(quantity) * int(month) * 25
            elif int(v) == 15:
                price = int(quantity) * int(month) * 75
            elif int(v) == 19:
                price = int(quantity) * int(month) * 95


            data = {'name': name,
                    'lastname': lastname,
                    'E_mail': E_mail,
                    'tel': tel,
                    'address': address,
                    'month': month,
                    'v': v,
                    'quantity': quantity,
                    'price': price,
            }
            return render(request, 'order.html', context=data)
        else:
            print('Ошибочка')
            # anketa = Creat_form()  # анкета это экземпляр этого класса
            data = {'form': anketa}  # переменная для вывода в html здесь выводит старую форму с ошибками
            return render(request, 'forma.html', context=data)

    else:
        anketa = Creat_form() # анкета это экземпляр этого класса
        data = {'form': anketa} # переменная для вывода в html
        return render(request, 'forma.html', context=data)