from django.shortcuts import render, redirect, get_object_or_404
from second.models import Post, StudentId, Attendance, Images, Food
from second.models import Post, StudentId, Attendance, Images, Routine, Notice, Absentday, Presentday
from django.contrib import messages
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
# Create your views here.
from .forms import UserUpdateForm, ProfileUpdateForm, StudentRegisterForm, AttendanceForm, RoutineForm, FoodForm, AbsentForm, PresentForm
from django.core.paginator import Paginator
from django.forms import modelformset_factory
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def routine(request):
    context = {
        'routine': Routine.objects.all()
    }

    return render(request, 'routine.html', context)


@login_required
def addroutine(request):
    form = RoutineForm(request.POST)

    if request.method == 'POST':
        if form.is_valid():
            form.save()

            return redirect('routine')

    context = {
        'form': form,
    }
    return render(request, 'addroutine.html', context)


def food(request):
    context = {
        'food': Food.objects.all()
    }

    return render(request, 'food.html', context)


@login_required
def addfood(request):
    formf = FoodForm(request.POST)

    if request.method == 'POST':
        if formf.is_valid():
            formf.save()

            return redirect('food')

    context = {
        'formf': formf,
    }
    return render(request, 'add_food.html', context)


def home(request):
    context = {
        'posts': Post.objects.all(),
    }
    return render(request, 'home.html', context)


@login_required
def registerchild(request):
    context = {
        'stid': StudentId.objects.all(),
    }
    return render(request, 'registerchild.html', context)


class RoutineListView(ListView):
    model = Routine
    template_name = 'routine.html'
    context_object_name = 'routine'


class RoutineDetailView(DetailView):
    model = Routine
    template_name = 'routine_detail.html'


@login_required
def addchild(request):
    formreg = StudentRegisterForm(request.POST)
    formreg1 = AttendanceForm(request.POST)

    if request.method == 'POST':
        if formreg.is_valid():
            formreg.save()
            name = formreg.cleaned_data.get('full_name')
            roll = formreg.cleaned_data.get('roll')
            childid = formreg.cleaned_data.get('childid')
            formreg1.save()
            return redirect('registerchild')

    context = {
        'formreg': formreg,
    }
    return render(request, 'addchild.html', context)


def attendance(request):

    forma = AbsentForm(request.POST)
    formp = PresentForm(request.POST)
    if 'absent' in request.POST:
        if forma.is_valid():
            forma.save()
            return redirect('attendance')
    if 'present' in request.POST:
        if formp.is_valid():
            formp.save()
            return redirect('attendance')

    context = {
        'students': Attendance.objects.all(),
        'forma': forma,
        'formp': formp
    }
    return render(request, 'attendance.html', context)


class AttendanceDetailView(DetailView):
    model = Attendance
    template_name = 'attendance_detail.html'


def postsandnotices(request):
    post_list = Post.objects.all()
    paginator = Paginator(post_list, 4)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'posts': page_obj,
        'notices': Notice.objects.all().order_by('-date_posted'),

    }

    return render(request, 'home.html', context)


class UserPostListView(ListView):
    model = Post
    template_name = 'user_posts.html'
    context_object_name = 'posts'
    paginate_by = 4

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'


class NoticeDetailView(DetailView):
    model = Notice
    template_name = 'notice_detail.html'


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = "/home/home"

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class NoticeDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Notice
    success_url = "/home/home"

    def test_func(self):
        notice = self.get_object()
        if self.request.user == notice.author:
            return True
        return False


class PostCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Post
    fields = ['title', 'content', 'photo']
    template_name = 'post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user

        return super().form_valid(form)

    def test_func(self):
        if self.request.user.last_name == 'teacher':
            return True
        return False


class NoticeCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Notice
    fields = ['title', 'content']
    template_name = 'notice_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user

        return super().form_valid(form)

    def test_func(self):
        if self.request.user.last_name == 'teacher':
            return True
        return False


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content', 'photo']
    template_name = 'notice_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class NoticeUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Notice
    fields = ['title', 'content']
    template_name = 'notice_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        notice = self.get_object()
        if self.request.user == notice.author:
            return True
        return False


# def profile(request):
    # return render(request,'users/profile.html')

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'profile.html', context)


class RoutineUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Routine
    fields = ['day', 'ten_ten45', 'ten45_eleven30', 'eleven45_twelve30',
              'twelve30_one15', 'two_two45', 'two45_three30']
    template_name = 'addroutine.html'

    def form_valid(self, form):
        return super().form_valid(form)

    def test_func(self):
        routine = self.get_object()
        return True
