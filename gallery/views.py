from django.shortcuts import render
from django.http  import HttpResponse,Http404,HttpResponseRedirect
from .models import Image, Location, Category
# Create your views here.

def index(request):
    images =Image.objects.all()
    return render(request, 'index.html',{"images":images})

def search_results(request):
    if 'image' in request.GET and request.GET['image']:
        search_input = request.GET.get('image')
        searched_images = Image.search_by_category(search_input)
        message = f"{search_input}"

        return render(request, 'search.html', {"message":message, "images":searched_images})

    else:
        message = "Please input something in the search field"
        return render(request, 'search.html', {'message':message})

def get_image_by_id(request,image_id):
    try: 
        images = Image.objects.get(id = image_id)
    except DoesNotExist:
        raise Http404()
    return render(request,"image.html", {"image":images})