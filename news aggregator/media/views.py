from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.shortcuts import render, redirect,HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import *
import requests
import json

#registration function to register me.
def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "media/register.html", {
                "message": "Type your passwords again."
            })

        # Attempts to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "media/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "media/register.html")

#login view for the login page to get in.
def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "media/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "media/login.html")

#The 1st news feed of stuff going on around the world.)
def index(request):
    main_API = requests.get("https://newsapi.org/v2/top-headlines?q=us&q=uk&q=asia&from=2021-05-05&to=2021-05-020&sortBy=popularity&apiKey=3286baaa16554442bae85d7b68ce5ff4")
    api = json.loads(main_API.content)
    return render(request, "media/index.html",{"api":api})


#For each API call I made a different function because easier to recognise and use through the urls.py
#The "african news" gets news from API on other events of the continent.
def news(request):
    main_API = requests.get("https://newsapi.org/v2/everything?q=africa&from=2021-05-05&to=2021-05-020&sortBy=popularity&apiKey=3286baaa16554442bae85d7b68ce5ff4")
    api = json.loads(main_API.content)
    if request.user.is_authenticated:
        return render(request, "media/News/news.html",{"api":api})
    else:
        return HttpResponseRedirect(reverse("login"))

#the API parsing through for the SA business section.
def news_business(request):
    main_API = requests.get("https://newsapi.org/v2/top-headlines?country=za&category=business&apiKey=3286baaa16554442bae85d7b68ce5ff4")
    api = json.loads(main_API.content)
    if request.user.is_authenticated:
        return render(request, "media/News/news_business.html",{"api":api})
    else:
        return HttpResponseRedirect(reverse("login"))

#the API parsing through for the SA politics section.
def news_politics(request):
    main_API = requests.get("https://newsapi.org/v2/top-headlines?country=za&category=politics&apiKey=3286baaa16554442bae85d7b68ce5ff4")
    api = json.loads(main_API.content)
    if request.user.is_authenticated:
        return render(request, "media/News/news_politics.html",{"api":api})
    else:
        return HttpResponseRedirect(reverse("login"))

#the API parsing through for the SA technology section
def news_technology(request):
    main_API = requests.get("https://newsapi.org/v2/top-headlines?country=za&category=technology&apiKey=3286baaa16554442bae85d7b68ce5ff4")
    api = json.loads(main_API.content)
    if request.user.is_authenticated:
        return render(request, "media/News/news_technology.html",{"api":api})
    else:
        return HttpResponseRedirect(reverse("login"))
