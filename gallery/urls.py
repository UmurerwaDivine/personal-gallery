from django.conf.urls import url
from . import views

from django.conf.urls.static import static
from django.conf import settings


urlpatterns=[
    url('^$',views.one_image,name = 'image'),
     url(r'^search/', views.search_results, name='search_results'),
    #  url(r'',views.image,name ='image')

   
    

]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)