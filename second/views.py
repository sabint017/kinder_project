from django.shortcuts import render
from second.models import Post
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
<<<<<<< HEAD
from users.models import User_parents, User_teachers
from django.contrib.auth.decorators import login_required
=======
>>>>>>> b0b85583e640e0876e2688156392cc8933d9c656
# Create your views here.


def home(request):
    context = {
        'posts': Post.objects.all(),
    }
    return render(request, 'home.html', context)


class PostListView(ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'posts'
    ordering = [
        '-date_posted'
    ]


class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = "/home/home"

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


#def profile(request):
   # return render(request,'users/profile.html')

@login_required
def profile(request):
    return render(request,'profile.html')