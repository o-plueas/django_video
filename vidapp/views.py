# video_app/views.py

from django.shortcuts import render, redirect
from .forms import VideoUploadForm
from .models import Video

def upload_video(request):
    if request.method == 'POST':
        form = VideoUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('video_list')
    else:
        form = VideoUploadForm()
    
    return render(request, 'vidapp/index.html', {'form': form})

def video_list(request):
    videos = Video.objects.all()
    return render(request, 'vidapp/vidlist.html', {'videos': videos})
