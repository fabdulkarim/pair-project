from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

app_name = 'espn'
urlpatterns = [
    path('', views.index, name='index'),
    # path('football', views.football, name='football'),
    # path('nfl', views.football, name='nfl'),
    # path('nba', views.nba, name='nba'),
    # path('football/<slug:foo>', views.footballitem, name='footballitem'),
    path('<str:sportstr>', views.sport , name='sport'),

    # path('<int:foo>', views.peritem , name='peritem'),

    # #routing coba
    path('<int:new_id>', views.news, name='news')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)