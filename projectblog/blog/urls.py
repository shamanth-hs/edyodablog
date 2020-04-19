from django.urls import path
from blog.views import PostDetailView,PostListView,CategoryView,PostFormView,PostFormUpdateView

urlpatterns = [
     path("post/addpost",PostFormView.as_view()),
     path("posts/<slug:slug>",PostFormUpdateView.as_view()),
    path("",PostListView.as_view(),name="post-detail"),
    path("<slug:slug>",PostDetailView.as_view(),name="post-detail"),
    path("category/<category>",CategoryView.as_view(),name="post-detail-category"),
   
]
