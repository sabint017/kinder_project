from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegistrationForm, User_p, User_t


def register_parent(request):
    if request.method == 'POST':
        form1 = UserRegistrationForm(request.POST)
        form_parents = User_p(request.POST)

        if form1.is_valid() and form_parents.is_valid():
            user=form1.save()
            profile= form_parents.save(commit=False)
            profile.user=user
            profile.save()

            username = form1.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}')
            return redirect('login')
    else:
        form1 = UserRegistrationForm()
        form_parents = User_p()

   
    return render(request, 'register_parent.html', {'form1': form1, 'form_parents':form_parents})


def register_teacher(request):
    if request.method == 'POST':
        form2 = UserRegistrationForm(request.POST)
        form_teachers = User_t(request.POST)
        if form2.is_valid() and form_teachers.is_valid():
            user=form2.save()
            profile1= form_teachers.save(commit=False)
            profile1.user=user
            profile1.save()

            username = form2.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}')
            return redirect('login')
    else:
        form2 = UserRegistrationForm()
        form_teachers = User_t()


    return render(request, 'register_teacher.html', {'form2': form2, 'form_teachers':form_teachers})



# Create your views here.
