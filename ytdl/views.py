from django.shortcuts import get_object_or_404, render , redirect
from django.urls import reverse
from django.views.generic import TemplateView , FormView , View
from .models import Video
from .forms import SearchItem
from pytube import YouTube
from django.core.files.base import ContentFile


class HomeView(TemplateView):
    template_name = 'ytdl/home.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['videos'] = Video.objects.all()
        return context
    
# class SearchUrlView(View):
#     template_name = 'ytdl/search.html'
#     def post(self , request):
#         url = request.POST.get('search')
#         try:
#             yt = YouTube(url)

#             video = yt.streams.get_highest_resolution()

#             output_path = 'media/ytdl/video/'
#             file_name = f"{yt.title}.mp4" 

#             video.download(output_path)

#             file = video.download(output_path)

#             video_obj = Video.objects.create(video=file , title=file_name , link=video.url)
#             video_obj.save()
#             print("ویدیو با موفقیت دانلود شد!")
#             return redirect(reverse('ytdl:home'))  
#         except Exception as e:
#             print("خطا در دانلود ویدیو:", str(e))
#             return redirect(reverse('ytdl_api:ytdl'))
    
#     def get(self , request):
#         return render(request , self.template_name , {})
    
# def ytdl_search(request):
#     context = {'errors' : []}
#     if request.method == 'POST' and request.FILES["video"]:
#         url = request.POST.get('search')
#         try:
#             yt = YouTube(url)

#             video = yt.streams.get_highest_resolution()

#             output_path = 'media/ytdl/video/'
#             file_name = f"{yt.title}.mp4" 

#             video.download(output_path, filename=file_name)

#             file_path = output_path + file_name
#             with open(file_path, 'rb') as f:
#                 file_content = f.read()
#             content_file = ContentFile(file_content, name=file_name)

#             video_obj = Video(video=content_file , title=file_name , link=video.url)
#             video_obj.save()
#             print("ویدیو با موفقیت دانلود شد!")
#             return redirect(reverse('ytdl:home'))  
#         except Exception as e:
#             print("خطا در دانلود ویدیو:", str(e))
#             return redirect(reverse('ytdl_api:ytdl'))
#     return render(request , 'ytdl/search.html')

class SearchUrlView(View):
    template_name = 'ytdl/search.html'
    def post(self, request):
        url = request.POST.get('search')
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
            video_obj.video.data = yt.streams
            video_obj.link = ytdl
            video_obj.save()

            video_objects = get_object_or_404(Video , id=video_obj.pk)

            print("ویدیو با موفقیت دانلود شد!")
            return render(request , 'ytdl/detailpage.html' , {'obj':video_objects}) 
        except Exception as e:
            print("خطا در دانلود ویدیو:", str(e))
            return redirect(reverse('ytdl_api:ytdl'))
    def get(self , request):
        return render(request , self.template_name , {})

class AboutView(TemplateView):
    template_name = 'ytdl/about.html'