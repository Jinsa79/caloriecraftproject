from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

from django.conf import settings
from django.conf.urls.static import static


#URLconfのURLパターンを逆引きできるようにアプリ名を登録
app_name = 'caloriecraft'

#URLパターンを登録するためのリスト
urlpatterns = [
    
    path('', views.IndexView.as_view(), name='index'),
    path('search/', views.search, name='search'),

    #
    #
    #
#    path('caloriecraft-detail/<int:pk>/', views.CalorieCraftDetail.as_view(), name='caloriecraft-detail'),
]

urlpatterns += static(

    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)