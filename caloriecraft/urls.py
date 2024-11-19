from django.urls import path
from . import views

#URLconfのURLパターンを逆引きできるようにアプリ名を登録
app_name = 'caloriecraft'

#URLパターンを登録するためのリスト
urlpatterns = [
    #http(s)://ホスト名/以下のパスが''(無し)の場合
    #viewsモジュールのIndexViewを実行
    #URLパターン名は'index'
    path('', views.IndexView.as_view(), name='index'),

    #
    #
    #
#    path('caloriecraft-detail/<int:pk>/', views.CalorieCraftDetail.as_view(), name='caloriecraft-detail'),
]