from django.urls import path , re_path
from .apiview import YtdlAPIView

app_name = 'ytdl_api'

urlpatterns = [
    path('' , YtdlAPIView.as_view() , name='ytdl'),
]