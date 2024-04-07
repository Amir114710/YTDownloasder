from django.urls import path , re_path
from .views import *

app_name = 'ytdl'

urlpatterns = [
    path('' , HomeView.as_view() , name='home'),
    path('search' , SearchUrlView.as_view() , name='search'),
    path('about' , AboutView.as_view() , name='about'),
]