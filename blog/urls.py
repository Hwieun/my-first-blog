from django.urls import path
from . import views

urlpatterns = [
#root url에 post_list라는 view 할당 #name에 넣은 것은 url에 이름을 붙인 것으로, 뷰를 식별
    path('', views.post_list, name='post_list'),
]
