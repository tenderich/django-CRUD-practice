from django.shortcuts import render
from django.utils import timezone

from django.urls import reverse_lazy
from django.views.generic.list import ListView #데이터 보여주기
from django.views.generic.detail import DetailView #디테일 보여주기
from django.views.generic.edit import CreateView, UpdateView, DeleteView #데이터 생성/업뎃/삭제
from .models import ClassBlog

# Create your views here.

#디폴트로 정해진 템플릿 이름이 있어요!

#html 템플릿 : 블로그 리스트 담은 html : (소문자모델)_list.html
class BlogView(ListView): 
    #이름을 디폴트가 아닌 것으로 바꿔주는 것
    template_name = 'classcrud/list.html'
    #만약 객체가 그냥 all로 쓰면 안되는경우라면?
    context_object_name= 'blog_list'
    model = ClassBlog

#html 템플릿 : form(입력공간)을 갖고있는 html : (소문자모델)_form.html
class BlogCreate(CreateView):
    model = ClassBlog
    fields = ['title','body']
    success_url = reverse_lazy('list')

#html 템플릿 : 상세페이지 담은 html : (소문자모델)_detail.html
class BlogDetail(DetailView):
    context_object_name = 'blogpost'
    model = ClassBlog

#html 템플릿 : form(입력공간)을 갖고있는 html : (소문자모델)_form.html
class BlogUpdate(UpdateView):
    model = ClassBlog
    fields = ['title','body']
    success_url = reverse_lazy('list')

#html 템플릿 : 진짜 지우려고? : (소문자모델)_confirm_delete.html
class BlogDelete(DeleteView):
    model = ClassBlog
    success_url = reverse_lazy('list')