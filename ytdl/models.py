from django.db import models

class Video(models.Model):
    video = models.FileField(upload_to='ytdl/video/' , null=True , blank=True , verbose_name='ویدیو')
    link = models.FileField(upload_to='ytdl/video/' , null=True , blank=True , verbose_name='لینک دانلود')
    title = models.CharField(max_length=580 , null=True , blank=True , verbose_name='نام ویدیو')
    discription = models.TextField(null=True , blank=True , verbose_name='توضیحات')
    
    class Meta:
        verbose_name='ویدیو'
        verbose_name_plural='ویدیو ها'