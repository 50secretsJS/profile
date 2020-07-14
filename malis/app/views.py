from django.shortcuts import render
from django.http import HttpResponse
from .models import photos
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator


def home(request):
    return render(request,'app/home.html')
    

def content(request):
    photo=photos.objects.all()

    paginator = Paginator(photo,3)
    page_number = request.GET.get('page')
    paged_photo = paginator.get_page(page_number)
    
    contex={
     'photo':paged_photo,
     'ged_photo':paged_photo
    }
    
    
    return render(request,'app/content.html',contex,)
