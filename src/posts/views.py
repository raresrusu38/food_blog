from django.shortcuts import get_object_or_404, render
from .models import Post, Category
from django.views.generic import ListView, DetailView

# Create your views here.

class IndexView(ListView):
    template_name = 'posts/index.html'
    model = Post
    context_object_name = 'posts'
    
    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        return context
    
    
class PostDetail(DetailView):
    template_name = 'posts/post-detail.html'
    model = Post
    context_object_name = 'single'
    
    
    def get_context_data(self, **kwargs):
        context = super(PostDetail, self).get_context_data(**kwargs)
        return context
    

class CategoryDetail(ListView):
    model = Post
    template_name = 'categories/category-detail.html'
    context_object_name = 'posts'
    
    def get_queryset(self):
        self.category = get_object_or_404(Category, pk=self.kwargs['pk'], slug=self.kwargs['slug'])
        return Post.objects.filter(category=self.category).order_by('-id')
    
    def get_context_data(self, **kwargs):
        context = super(CategoryDetail, self).get_context_data(**kwargs)
        self.category = get_object_or_404(Category, pk=self.kwargs['pk'], slug=self.kwargs['slug'])
        context['category'] = self.category
        return context
