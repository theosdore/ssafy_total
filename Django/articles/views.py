from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm
from django.contrib.auth.decorators import login_required


# 게시판 메인 페이지 (GET)
def index(request):
    # DB의 모든 articles 를 context 로 전달
    articles = Article.objects.all()

    context = {
        'articles': articles,
    }
    response = render(request, "articles/index.html", context)
    response.set_cookie(
        key = "username",
        value = "yuyeon"
    )

    return render(request, "articles/index.html", context)


# 생성 페이지 (GET)
# 게시물 생성 (POST)
@login_required
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = ArticleForm()

    context = {
        'form': form,
    }
    
    return render(request, "articles/create.html", context)


