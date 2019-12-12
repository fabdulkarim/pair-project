from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Berita, Detail, Team

# Create your views here.
def index(request):
    berita_object = Berita.objects.all().order_by('-createdat')
    return render(request, 'espn/index.html', {'berita_object':berita_object})

# def football(request):
#     # list_id = Detail.objects.filter(sport='Football').berita_id
    
#     football_news = Berita.objects.filter(sport='Football').order_by('createdat')

#     return render(request, 'espn/index.html', {'berita_object':football_news})

# def nfl(request):
#     # list_id = Detail.objects.filter(sport='Football').berita_id
    
#     nfl_news = Berita.objects.filter(sport='NFL').order_by('createdat')

#     return render(request, 'espn/index.html', {'berita_object':nfl_news})

# def nba(request):
#     # list_id = Detail.objects.filter(sport='Football').berita_id
    
#     nba_news = Berita.objects.filter(sport='NBA').order_by('createdat')

#     return render(request, 'espn/index.html', {'berita_object':nba_news})

def sport(request, sportstr):
    sport_news = Berita.objects.filter(sport=sportstr).order_by('-createdat')

    return render(request, 'espn/index.html', {'berita_object':sport_news})

def peritem(request, foo):
    # pembatas = Berita.objects.get(link=foo).id
    # peritem_news = Berita.objects.filter(sport=bar).filter(id__lte=foo).order_by('-createdat')
    peritem_news = Berita.objects.filter(id__lte=foo).order_by('-createdat')
    print(foo)
    peritem_news = Berita.objects.get(pk=foo)
    print(peritem_news)
    return render(request, 'news.html', {'baru':peritem_news})

# def slugify(arr1):
#     return '-'.join(arr.split(' ')).lower()

def news(request, new_id):
    new = Berita.objects.get(pk=new_id)
    var = {'new' : new}
    return render(request, 'espn/news.html', var)