from django.urls import path, include
from .import views
from django.conf import settings
from django.conf.urls.static import static
from .views import *


urlpatterns = [
    path('', views.index,name='index'),
    path('home',views.index, name='home'),
    path('tamil_short_stories/<slug:slug>/',views.tamil_short_stories,name='tamil_short_stories'),
    path('search',views.search, name='search'),
    path('about',views.about, name='about'),
    path('contact',views.contact, name='contact'),
    path('login',views.login, name='login'),
    path('register',views.register, name='register'),
    path('rr',views.rr,name='rr'),
    path('message',views.message,name='message'),
    path('logout', views.logout, name='logout'),
    path('userpost',views.userpost,name='userpost'),
    path('privacy',views.privacy, name='privacy'),
    path('terms',views.terms, name='terms'),

   
   
   
     
     

    ]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)