from django.shortcuts import render
from .models import Buyer, Game
from .forms import UserRegister


def platform(request):
    return render(request, 'platform.html')


def menu(request):
    game_dict = Game.objects.all()
    return render(request, 'games.html', {'games': game_dict})


def cart(request):
    return render(request, 'cart.html')


def sign_up_by_html(request):
    info = {}
    users = Buyer.objects.all()
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = int(request.POST.get('age', 0))

        if username in users:
            info['error'] = 'Пользователь уже существует'
        elif age < 18:
            info['error'] = 'Вы должны быть старше 18'
        elif password != repeat_password:
            info['error'] = 'Пароли не совпадают'
        else:
            info['message'] = f'Приветствуем, {username}!'
    else:
        info['username'] = request.POST.get('username', '')
    return render(request, 'registration_page.html', info)
