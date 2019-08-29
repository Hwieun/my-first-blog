from django.shortcuts import render
from django.utils import timezone
from .models import Post
#redirect 새 글 작성하고 저장 후에 post_detail 페이지로 이동할 수 있게
from django.shortcuts import render, get_object_or_404, redirect
from .forms import PostForm

def post_list(request):
    #posts 가 QuerySet
    posts = Post.objects.order_by('published_date')

    return render(request, 'blog/post_list.html', {'posts':posts})

def post_detail(request, pk) :
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post':post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            #바로 Post 모델에 저장하지 말라는 의미. 작성자 추가한 후에 저장
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()

    return render(request, 'blog/post_edit.html', {'form':form})

def post_edit(request, pk):
    #없으면 404
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        #post_new와 다르게 전에 있던 데이터를 불러와서 form 구성
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)

    return render(request, 'blog/post_edit.html', {'form':form})
