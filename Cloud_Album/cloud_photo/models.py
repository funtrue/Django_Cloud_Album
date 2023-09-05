from django.db import models

class Photo(models.Model):
    image   = models.ImageField(upload_to='photo/%Y%m%d/',verbose_name="照片")
    created_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")

    def __str__(self):
        return self.image.name
    
    class Meta:
        verbose_name = "照片模型"
        ordering = ('-created_time',)