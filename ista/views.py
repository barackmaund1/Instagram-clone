from django.shortcuts import render, get_object_or_404,reverse
from .models import Image,Comment
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .forms import ImageForm,CommentForm
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
# Create your views 

class PostListView(LoginRequiredMixin,ListView):
    model = Image
    template_name = 'ista/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'images'
    ordering = ['-date_posted']
    paginate_by = 5  
   
class UserPostListView(ListView,LoginRequiredMixin):
    model = Image
    # <app>/<model>_<viewtype>.html image_list.html
    context_object_name = 'images'
    paginate_by = 7

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Image.objects.filter(author=user).order_by('-date_posted')

class PostDetailView(DetailView,LoginRequiredMixin):
    model = Image  
    context_object_name = 'image'

    
     
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Image
    form_class=ImageForm
    # success_url = 'user/<str:username>'
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Image
    form_class=ImageForm
    

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Image
    success_url = '/'
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class CreatePost(LoginRequiredMixin, CreateView):
    model = Image
    fields = ['photo', 'caption', 'location']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class CreateComment(LoginRequiredMixin, CreateView):
    model = Comment
    fields = ['comment']
    success_url = '/'
    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.image_id = self.kwargs['pk']
        return super().form_valid(form)



