from django.shortcuts import render,redirect
from django.http import HttpRequest, HttpResponse
from .forms import PostCreationForm
from .models import Post


# Create your views here.


def index(request:HttpRequest):
    posts = Post.objects.all()
        
    context = {
        "posts": posts
    }
    return render(request,'index.html', context)

def about(request):
    context = {
        "tittle": "About Page"
    }
    return render(request, 'about.html', context)

def services(request):
    context = {
        "tittle": "About Page"
    }
    return render(request, 'services.html', context)

def create_post(request):
    form = PostCreationForm()
    
    if request.method == "POST":
        form = PostCreationForm(request.POST, request.FILES)
        
        if form.is_valid():
            form.save()
            
            return redirect('post_home')
    context={
        'form': form
    }
    return render (request,"create_post.html", context)
    
    
    
    # tittle = (data['tittle'])
    #     content = (data['content'])
    #     author = (data['author'])
        
    #     new_post = Post(
    #         tittle = tittle,
    #         content = content,
    #         author = author
    #     )
    #     new_post.save()
    
    
    
    