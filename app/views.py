from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.db.models import Q
from datetime import datetime
from app.models import Word, General, CustomUser, Category
from django.shortcuts import render
import random


import openpyxl
from pathlib import Path

def testqilish(request):
    if request.user.id == 1:
        xlsx_file = Path('4000-most-common-english-words-xlsx.xlsx')
        wb_obj = openpyxl.load_workbook(xlsx_file)

        # Read the active sheet:
        sheet = wb_obj.active

        for row in sheet.iter_rows(max_row=4342, min_row=7):
            data = General.objects.create(english=row[0].value)
            data.save()
        return HttpResponse("Test muvafaqqiyatli yakunlandi!")
    else:
        return redirect('login')

def registratsiya(request):
    if request.user.is_authenticated:
        return redirect('new_word')
    else:
        if 'orqaga' in request.POST:
            return redirect('login')
        elif 'saqlash' in request.POST:
            # form = ImageForm(request.POST, request.FILES)
            # if form.is_valid():
            #     print(form)
            #     form.save()

            data = request.POST
            username = data['username']
            ism = data['ism']
            print(data.get('rasm'), 23523523523)
            image = request.FILES['rasm'] if data.get('rasm') else None
            parol = data['password']
            paroltak = data['password2']

            if username and ism and parol and paroltak:
                if parol == paroltak:
                    user = CustomUser.objects.create_user(username=username, password=parol, first_name=ism, image=image)
                    user.save()
                    auth_login(request, user)
                    return redirect('new_word')
                else:
                    messages.error(request, "Parollarni bir hil kiriting.", "danger")
            else:
                messages.error(request, "Ma'lumot to'laligicha kiritilmagan.", "danger")
        # else:
        # form = ImageForm()
        return render(request, 'registratsiya.html')


def login(request):
    if request.user.is_authenticated:
        return redirect('new_word')
    else:
        if 'register' in request.POST:
            return redirect('registratsiya')
        if request.method == "POST":
            data = request.POST
            username = data['username']
            parol = data['password']
            user = authenticate(request, username=username, password=parol)
            if user is not None:
                auth_login(request, user)
                return redirect('new_word')
            elif username == '' or parol == '':
                messages.error(request, "Bo'shliqni to'ldiring", "info")
            else:
                messages.error(
                    request, "Username yoki password xato", "danger")

        return render(request, 'login.html')


def logout(request):
    auth_logout(request)
    return redirect('login')


def add(request):
    if not request.user.is_authenticated:
        return redirect('login')
    else:
        if request.method == "POST":
            data = request.POST
            if not Word.objects.filter(english=data['eng'], created_user=request.user.id):
                now = datetime.now()
                oy_raqam = {1: 'yanvar', 2: 'fevral', 3: 'mart', 4: 'aprel', 5: 'may', 6: 'iyun', 7: 'iyul',
                            8: 'avgust',
                            9: 'sentabr', 10: 'oktabr', 11: 'noyabr', 12: 'dekabr'}
                oy = oy_raqam[now.month]
                category = str(now.day) + '-' + oy + ' ' + str(now.year) + '-yil'
                if Category.objects.filter(name=category).count() == 0:
                    Category.objects.create(name=category, created_user_id=request.user.id)
                r = Category.objects.get(name=category)
                id = Category.objects.get(name=category).id
                obj = Word.objects.create(english=data['eng'],
                                          uzbek=data['uzb'],
                                          category=r,
                                          created_user=request.user)

                messages.success(request, obj.english +
                                 " muvaffaqiyatli qo'shildi")

            else:
                messages.info(request, data['eng'] + " so'zi jadvalda bor!")

        words = Word.objects.filter(
            created_user=request.user).order_by('-id')[:10]

        context = {
            "words": words,
            "current_add": "active",
            "title": "So'z qo'shish"
        }
        return render(request, 'add.html', context)


def delete(request, pk):
    if not request.user.is_authenticated:
        return redirect('login')
    else:
        obj = Word.objects.get(id=pk)
        if request.method == "POST":
            name = obj.english
            obj.delete()
            messages.success(request, name + " muvaffaqiyatli o'chirildi!")
            return redirect('new_word')

        context = {
            "word": obj,
            "title": "So'z o'chirish"

        }
        return render(request, 'delete.html', context)


def edit(request, pk):
    if not request.user.is_authenticated:
        return redirect('login')
    else:
        obj = Word.objects.get(id=pk)
        if request.method == "POST":
            obj.english = request.POST['eng']
            obj.uzbek = request.POST['uzb']
            obj.save()
            messages.success(request, obj.english +
                             " muvaffaqiyatli o'zgartirildi!")
            return redirect('new_word')

        context = {
            "word": obj,
            "title": "So'z taxrirlash"

        }
        return render(request, 'edit.html', context)


def search(request):
    if not request.user.is_authenticated:
        return redirect('login')
    else:
        text = request.GET.get('search', '')

        if request.user.is_superuser:
            words = Word.objects.filter(
                Q(english__icontains=text) | Q(uzbek__icontains=text)).order_by('-id')
        else:
            words = Word.objects.filter(created_user=request.user).filter(
                Q(english__icontains=text) | Q(uzbek__icontains=text)).order_by('-id')
        context = {
            "words": words,
            "current_search": "active",
            "title": "So'z qidirish"

        }
        return render(request, 'search.html', context)


def test(request):
    if not request.user.is_authenticated:
        return redirect('login')
    else:
        if 'test1' in request.POST:
            # messages.get_messages(request, )
            olish = 0
            soni = request.POST['soni']
            question = General.objects.filter(status=1)
            while olish != soni:
                pass

            return HttpResponse('<p style="font-size: 30px;">Success1</p>')

        if 'test2' in request.POST:
            # messages.get_messages(request, )
            return HttpResponse('<p style="font-size: 30px;">Success2</p>')
            # for i in

        if 'test3' in request.POST:
            # messages.get_messages(request, )
            return HttpResponse('<p style="font-size: 30px;">Success3</p>')
            # for i in
        context = {
            "current_test": "active",
            "title": "Test qilish"

        }
        return render(request, 'test.html', context)


def toplam(request):
    if request.user.is_authenticated == False:
        return redirect('login')
    a = Category.objects.filter(created_user_id=request.user.id)
    b = ''
    if a.count() == 0:
        b = "Kategoriyalar yo'q"
    category = ''
    for t in a:
        category = t
        break
    if request.method == 'POST':
        id = request.POST['submit']
        category = Category.objects.get(id=id)
        words = Word.objects.filter(created_user_id=request.user.id, category=category)
    else:
        words = Word.objects.filter(english='Hello', uzbek='Salom')

    context = {
        'b': b,
        'cate': a,
        "current_toplam": "active",
        "title": "To'plamlar",
        'words': words,
        'categor': category
    }
    return render(request, 'toplam.html', context)
