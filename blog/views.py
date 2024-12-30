from django.http import HttpResponse
from django.shortcuts import render
from .models import Blogpost

# Create your views here.
def index(request):
    blog = Blogpost.objects.all()
    context = {'blog': blog}
    return render(request, 'blog/index.html',context)

def blogpost(request,id):
    blog = Blogpost.objects.filter(id=id)[0]
    context = {'blog': blog}
    return render(request,'blog/blogpost.html',context)