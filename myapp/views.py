from django.shortcuts import render
from myapp.models import Post

# Create your views here.

def post(request):
    
    all_post=Post.objects.all()

    contexts={
        "posts":all_post,
    }
    return render(request,'myapp/index.html',contexts)

def hello(request,pk):
    posts=Post.objects.get(pk=pk)

    context={
        'post':posts,
    
    }
    return render(request,"myapp/detail.html",context)

def navb(request):
    return render(request,'myapp/base.html')

def ga(request):
    return render(request,'myapp/gallery.html')

def co(request):
    return render(request,'myapp/contact.html')