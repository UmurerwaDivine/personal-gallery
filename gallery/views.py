from django.shortcuts import render
from django.http  import HttpResponse,Http404,HttpResponseRedirect
from .models import Image, Location, Category
# Create your views here.

def index(request):
    return render(request, 'index.html')

# def image(request):
    
    images =Image.all_images()
    return render(request,'index.html',{"images":images})
def search_results(request):

    if 'category' in request.GET and request.GET["category"]:
        search_term = request.GET.get("category")
        searched_images = Image.search_by_category(search_term)
        message = f"{search_term}"

        return render(request, 'templates/search.html',{"message":message,"images": searched_images})

    else:
        message = "You haven't searched for any term"
        return render(request, 'templates/search.html',{"message":message})

def one_image(request,id):
    try:
        images = Image.objects.get(id =id)
    except DoesNotExist:
        raise Http404()
    return render(request,"templates/image.html", {"images":images})
