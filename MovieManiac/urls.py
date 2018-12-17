"""MovieManiac URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from TestApp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home',homeView),
    path('signup',signupView),
    path('signout',signoutView),
    path('newlist',listView),
    path('addlist',addListView),
    path('watchlist',listing),
    path('forgot_password',forgot_password),
    path('profile',profileView),
    path('mylist',f),
    path('movie_profile',movie_profile_view),
    path('all_movie',all_movie),
    path('rated',after_rated),
    path('rate',rate),
    path('recommend',recommender),
    path('search',searchView),
    path('home2',renderHomePage),
    path('mylist2',mylist)
]
