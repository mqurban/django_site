from django.shortcuts import render

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def contact(request):
    return render(request, 'contact.html')
def home(request):
    return render(request, 'index.html')

def photo_detail(request):
    return render(request, 'photo-detail.html')

def video_detail(request):
    return render(request, 'video-detail.html')

