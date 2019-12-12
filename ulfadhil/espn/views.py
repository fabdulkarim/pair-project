from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Berita, Detail, Team

# Create your views here.
def index(request):
    berita_object = Berita.objects.all().order_by('createdat')
    return render(request, 'espn/index.html', {'berita_object':berita_object})

def football(request):
    # list_id = Detail.objects.filter(sport='Football').berita_id
    
    football_news = Berita.objects.filter(sport='Football').order_by('createdat')

    return render(request, 'espn/index.html', {'berita_object':football_news})

def nfl(request):
    # list_id = Detail.objects.filter(sport='Football').berita_id
    
    nfl_news = Berita.objects.filter(sport='NFL').order_by('createdat')

    return render(request, 'espn/index.html', {'berita_object':nfl_news})

def nba(request):
    # list_id = Detail.objects.filter(sport='Football').berita_id
    
    nba_news = Berita.objects.filter(sport='NBA').order_by('createdat')

    return render(request, 'espn/index.html', {'berita_object':nba_news})