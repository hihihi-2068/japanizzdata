from django.urls import path
from . import views
urlpatterns = [
    path('', views.get_home),
    path('home', views.get_home),
    path('login', views.get_login),
    path('forgotpassword', views.get_forgotpassword),
    path('register/', views.get_register),
    path('logout/',views.get_logout),
    path('characters/',views.get_characters),
    path('kanji/',views.get_kanji),
    path('vocabulary/',views.get_vocabulary),
    path('grammar/',views.get_grammar),
    path('account/',views.get_account),
]