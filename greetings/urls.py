"""
URL configuration for greetings project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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

from myapp.views import HelloWorldView,GoodMorningView,GoodAfternoonView,greetings_view,SelfIntroView,\
    ActorView,CourseDetailView



urlpatterns = [
    path('admin/', admin.site.urls),

    path("helloworld/",HelloWorldView.as_view()),

    path("morning/",GoodMorningView.as_view()),

    path("afternoon/",GoodAfternoonView.as_view()),

    path("greetings/",greetings_view),

    path("intro/",SelfIntroView.as_view()),

    path("actor/",ActorView.as_view()),

    path("course/",CourseDetailView.as_view())



]
