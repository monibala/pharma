from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

from blog.models import Blogs

# Create your views here.
def blog(request):
    blg = Blogs.objects.all()
    res = {'blg':blg}
    return render(request, 'blog.html',res)

def blogsingle(request,slug):
    data = Blogs.objects.get(slug=slug)
    res = {'data':data}
    return render(request, 'blogsingle.html',res)