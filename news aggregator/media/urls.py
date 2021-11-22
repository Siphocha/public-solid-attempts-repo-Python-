from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("register", views.register, name="register"),
    path("login", views.login_view, name="login"),
    path("news", views.news, name="news"),
    path("news_business", views.news_business, name="news_business"),
    path("news_politics", views.news_politics, name="news_politics"),
    path("news_technology", views.news_technology, name="news_technology")
]