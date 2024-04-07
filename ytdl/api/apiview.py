from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser
from rest_framework import status
from django.shortcuts import get_object_or_404
from .serializers import *
from pytube import YouTube
from django.core.files.base import ContentFile

class YtdlAPIView(APIView):
    serializer_class = YtdlSerializer
    parser_classes = [MultiPartParser]

    def post(self, request):
        data = request.data
        serializer = YtdlSerializer(data=data)
        if serializer.is_valid():
            url = serializer.data['url']
            try:
                yt = YouTube(url)

                video = yt.streams.get_highest_resolution()

                output_path = 'media/ytdl/video/'
                output_path2 = 'media/'
                file_name = f"{yt.title}.mp4"
                file_path = output_path + file_name
                video.download(output_path, filename=file_name)
                ytdl = video.download(output_path, filename=file_name)

                video_obj = Video()
                video_obj.title = yt.title
                video_obj.discription = yt.description
                video_obj.link = ytdl
                video_obj.save()
                seri = VideoSerializer(instance=video_obj)
                print("ویدیو با موفقیت دانلود شد!")
                return Response(seri.data, status=status.HTTP_200_OK)
            except Exception as e:
                print("خطا در دانلود ویدیو:", str(e))
                return Response("خطا در دانلود ویدیو", status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)