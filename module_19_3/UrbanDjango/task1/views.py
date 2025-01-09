from django.shortcuts import render
from django.http import HttpResponse
from .models import Buyer, Game


def platform(request):
    return render(request, 'platform.html')

# def games(request):
#     return render(request, 'fourth_task/games.html')

def menu(request):
    game_dict = {'games': ["Atomic Heart", "Cyberpunk 2077", "PayDay 77"]}
    context = {
        'game_dict': game_dict,
    }
    return render(request, 'games.html', context)



def cart(request):
    return render(request, 'cart.html')