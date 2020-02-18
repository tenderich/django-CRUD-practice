from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Blog
from .forms import NewBlog

# Create your views here.
def welcome(request):
    return render(request, 'funccrud/index.html')

def read(request):
    blogs = Blog.objects.all()
    return render(request, 'funccrud/funccrud.html', {'blogs':blogs})

def create(request):
    #REQUEST 의 형식으로 구분한다
    #새로운 블로그 글 저장하는 역할 == POST
    if request.method == 'POST':
        #새로 입력된 블로그 글 저장해주세요
        form = NewBlog(request.POST)
        if form.is_valid:
            post = form.save(commit=False)
            post.pub_date = timezone.now()
            post.save()
            return redirect('home')
    #글쓰기 페이지를 띄워주는 역할 == GET 
    else:
        #입력 받을수 있는 Form 띄워주세요
        form = NewBlog()

        return render(request, 'funccrud/new.html', {'form':form})

def update(request, pk):
    #어떤 블로그를 수정할지 해당 블로그 객체 가져오기
    blog = get_object_or_404(Blog, pk=pk)

    #해당하는 블로그 객체 pk에 맞는 입력공간 갖고오기
    #pk번째에 해당하는 블로그를 다시 쓸수있게 가져와
    form = NewBlog(request.POST, instance=blog)

    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'funccrud/new.html',{'form':form})

def delete(request, pk):
    blog = get_object_or_404(Blog, pk= pk)
    blog.delete()
    return redirect('home')