from django.shortcuts import render
from django.views.generic import DetailView,ListView,CreateView,UpdateView
from blog.models import Post,Category
from blog.forms import PostForm
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin,UserPassesTestMixin

# Create your views here.

class PostDetailView(DetailView):
    model = Post
    # queryset = Post.objects.filter(status = "P")
    template_name = "blog/details.html"

class PostListView(ListView):
    model = Post
    queryset = Post.objects.filter(status = "P")
    template_name = "blog/index.html"
    context_object_name = "posts"


    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs) 
        context['categories'] = Category.objects.all()
        # context['author'] = Author.objects.all()

        return context


class CategoryView(ListView):
    model = Post
    template_name = "blog/index.html"
    context_object_name = "posts"

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs) 
        context['categories'] = Category.objects.all()
        # context['author'] = Author.objects.all()

        return context

    def get_queryset(self):
        # self.category = get(Category, name=self.kwargs['category'])
        self.category = Category.objects.get(name =self.kwargs['category'])
        return Post.objects.filter(status = "P",category = self.category )

class PostFormView(LoginRequiredMixin,PermissionRequiredMixin, CreateView):
    # model = Post
    # fields = ['title','content','status','category','image','author']
    # success_url = 'posts'
    permission_required = 'blog.add_post'
    template_name = "blog/post.html"
    form_class = PostForm

    # def test_func(self,*args, **kwargs):
    #     slug = self.kwargs.get("slug")
    #     post = Post.objects.get(slug = slug)
    #     if self.request.user.get_username() == post.author.get_username():
    #         return True
    #     else:
    #         return False


class PostFormUpdateView(LoginRequiredMixin,PermissionRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Post
    form_class = PostForm
    template_name = "blog/post.html"
    permission_required = ('blog.add_post','blog.change_post')

    def test_func(self,*args, **kwargs):
        slug = self.kwargs.get("slug")
        post = Post.objects.get(slug = slug)
        if self.request.user.get_username() == post.author.get_username():
            return True
        else:
            return False


    

        