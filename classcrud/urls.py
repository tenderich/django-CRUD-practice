from django.urls import path
from . import views

urlpatterns = [
    #두번쨰 인자에서 blogview.as_view... 두번째 인자 class를 줄수 없으니께
    #두번째 인자 views.클래스이름.as_view()
    
    path('', views.BlogView.as_view(), name='list'),
    path('newblog/', views.BlogCreate.as_view(), name='new'),
    path('detail/<int:pk>', views.BlogDetail.as_view(), name='detail'),
    path('update/<int:pk>', views.BlogUpdate.as_view(), name='change'),
    path('delete/<int:pk>', views.BlogDelete.as_view(), name='del')
]