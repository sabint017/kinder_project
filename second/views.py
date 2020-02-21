from django.shortcuts import render, redirect, get_object_or_404
from second.models import Post, StudentId, Attendance, Images, Food, Result
from second.models import Post, StudentId, Attendance, Images, Routine, Notice, Absentday, Presentday, SID, Events
from django.contrib import messages
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
# Create your views here.
from .forms import UserUpdateForm, ResultForm, ProfileUpdateForm, StudentRegisterForm, AttendanceForm, RoutineForm, FoodForm, AbsentForm
from django.core.paginator import Paginator
from django.forms import modelformset_factory
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import datetime
from django.shortcuts import redirect
from django.contrib import messages


def routine(request):
    context = {
        'routine': Routine.objects.all()
    }

    return render(request, 'routine.html', context)


def result(request):

    context = {
        'results': Result.objects.all()
    }
    return render(request, 'result.html', context)


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


def addresult(request):
    form = ResultForm(request.POST)

    if request.method == 'POST':
        if form.is_valid():
            form.save()

            return redirect('result')

    context = {
        'form': form,
    }
    return render(request, 'addresult.html', context)


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
        'stid': SID.objects.all(),
    }
    return render(request, 'registerchild.html', context)


class RoutineListView(ListView):
    model = Routine
    template_name = 'routine.html'
    context_object_name = 'routine'


class RoutineDetailView(DetailView):
    model = Routine
    template_name = 'routine_detail.html'


class ResultDetail(DetailView):
    model = Result
    template_name = 'resultdetail.html'


def attendance(request):

    context = {
        'students': Attendance.objects.all(),
    }
    return render(request, 'attendance.html', context)


def present(request, id):
    student = Attendance.objects.get(id=id)
    student1 = Presentday.objects.filter(
        name=student, date=datetime.date.today())
    if student1.exists():
        messages.error(request, 'Attendance already done for today!')

    else:
        student1 = Presentday.objects.create(
            name=student, date=datetime.date.today())

    return redirect('attendance')


def presentdecrease(request, id):
    student = Attendance.objects.get(id=id)
    student1 = Presentday.objects.filter(
        name=student, date=datetime.date.today())
    student1.delete()
    return redirect('attendance')


def absent(request, id):
    student = Attendance.objects.get(id=id)
    student1 = Absentday.objects.filter(
        name=student, date=datetime.date.today())
    if student1.exists():
        messages.error(request, 'Attendance already done for today!')
    else:
        student1 = Absentday.objects.create(
            name=student, date=datetime.date.today())

    return redirect('attendance')


def absentdecrease(request, id):
    student = Attendance.objects.get(id=id)
    student1 = Absentday.objects.filter(
        name=student, date=datetime.date.today())
    student1.delete()
    return redirect('attendance')


class AttendanceDetailView(DetailView):
    model = Attendance
    template_name = 'attendance_detail.html'


def postsandnotices(request):
    post_list = Post.objects.all()

    context = {
        'posts': post_list,
        'notices': Notice.objects.all().order_by('-date_posted'),
        'events' : Events.objects.all().order_by('-date_posted'),

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
        if self.request.user.user_teachers != '':
            return True
        return False


class SIDCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = SID
    fields = ['full_name', 'roll', 'childid']
    template_name = 'addchild.html'

    def form_valid(self, form):
        form.instance.teacher = self.request.user

        return super().form_valid(form)

    def test_func(self):
        if self.request.user.user_teachers != '':
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
        if self.request.user.user_teachers != '':
            return True
        return False


class EventsDetailView(DetailView):
    model = Events
    template_name = 'events_detail.html'

class EventsDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Events
    success_url = "/home/home"

    def test_func(self):
        events = self.get_object()
        if self.request.user == events.author:
            return True
        return False


class EventsCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Events
    fields = ['title', 'content']
    template_name = 'events_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user

        return super().form_valid(form)

    def test_func(self):
        if self.request.user.user_teachers != '':
            return True
        return False

class EventsUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Events
    fields = ['title', 'content']
    template_name = 'events_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        events = self.get_object()
        if self.request.user == events.author:
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


class ResultUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Result
    fields = ['name', 'subject1', 'subject2', 'subject3',
              'subject4', 'grade', 'remarks']
    template_name = 'addresult.html'

    def form_valid(self, form):
        return super().form_valid(form)

    def test_func(self):
        result = self.get_object()
        return True
