from django.shortcuts import render
from .models import photos #import photos model

def index(request):
    # imports photos and save it in database
    photo = photos.objects.all()
    # adding context 
    ctx = {'photo':photo}
    return render(request, 'index.html', ctx)