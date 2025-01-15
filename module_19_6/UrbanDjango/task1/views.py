from django.core.paginator import Paginator
from django.shortcuts import render
from django.db.models.functions import Lower
from .models import Buyer, Game, News
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

        if users.filter(name__iexact=username.lower()).exists():
            info['error'] = 'Пользователь уже существует'
        elif age < 18:
            info['error'] = 'Вы должны быть старше 18'
        elif password != repeat_password:
            info['error'] = 'Пароли не совпадают'
        else:

            # запись в таблицу
            Buyer.objects.create(
                            name=username,
                            balance=0,
                            age=age)

            info['message'] = f'Приветствуем, {username}!'
    else:
        info['username'] = request.POST.get('username', '')
    return render(request, 'registration_page.html', info)

def news_page(request):
    news = News.objects.all().order_by('-date')
    paginator = Paginator(news, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'news.html', {'news': page_obj})