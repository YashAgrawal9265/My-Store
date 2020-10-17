from django.shortcuts import render,HttpResponse
from blog.models import Blogpost

# Create your views here.

def index(request):
    blogs = Blogpost.objects.all()
    params = {'blogs':blogs}
    return render(request,'blog/index.html',params)


def blogpost(request,myid):
    blog = Blogpost.objects.filter(post_id=myid)
    params = {'blog':blog[0]}
    return render(request,'blog/blogpost.html',params)