from django.urls import path
from . import views

app_name="articles"
urlpatterns = [
    path("", views.index, name="index"),  # Todo: 게시글 전체 조회  ( / )
    # 게시글 상세 조회  ( /<int:id>/ )
    path("create/", views.create, name="create"), # 게시글 작성  ( /create/ )
    # 게시글 수정  ( /<int:id>/update/ )
    # 게시글 삭제  ( /<int:id>/delete/ )
]
