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


def sign_up_by_django(request):
    info = {}
    users = Buyer.objects.all()
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']

            if username in users:
                info['error'] = 'Пользователь уже существует'
            elif age < 18:
                info['error'] = 'Вы должны быть старше 18'
            elif password != repeat_password:
                info['error'] = 'Пароли не совпадают'
            else:
                users.append(username)
                info['message'] = f'Приветствуем, {username}!'

    return render(request, 'registration_page.html', info)