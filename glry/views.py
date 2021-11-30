from django.shortcuts import render
from .models import photos, Location

# Create your views here.
def index(request):
    images = photos.objects.all()
    locations = Location.get_locations()
    return render(request, 'glrys/index.html', {'images': images[::-1], 'locations': locations})

def image_location(request, location):
    images = photos.filter_by_location(location)
    return render(request, 'glrys/address.html', {'location_images': images})

def search_results(request):
    if 'imagesearch' in request.GET and request.GET["imagesearch"]:
        gallery_category = request.GET.get("imagesearch")
        searched_images = photos.search_by_category(gallery_category)
        message = f"{gallery_category}"
        return render(request, 'glrys/search.html', {"message": message, "images": searched_images})
    else:
        message = "You haven't searched for any image category"
        return render(request, 'glrys/search.html', {"message": message})