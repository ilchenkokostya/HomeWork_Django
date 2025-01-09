from django.shortcuts import render
from django.http import HttpResponse
from .models import Buyer, Game


def platform(request):
    return render(request, 'platform.html')

def menu(request):
    game_dict = Game.objects.all()
    context = {
        'game_dict': game_dict,
    }
    return render(request, 'games.html', context)

def cart(request):
    return render(request, 'cart.html')