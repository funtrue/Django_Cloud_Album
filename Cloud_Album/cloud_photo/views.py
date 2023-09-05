from django.shortcuts import render
from cloud_photo.models import Photo

def home(request):
    photos  = Photo.objects.all()
    context = {'photos': photos}
    return render(request, 'cloud_photo/list.html', context)