
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login as auth_login
from django.contrib.auth import authenticate, logout
from .forms import TodoForm, loginform, taskeditform, todoregisterform
from .models import Todo

# user mainPage


def home(request):
    return render(request, 'home.html')


# user Registration


def registration(request):
    form = todoregisterform()
    if request.method == 'POST':
        form = todoregisterform(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "form saved")
            return redirect('login')
        else:
            form = todoregisterform()
            messages.error(request, "form not  saved")
    context = {'form': form}
    return render(request, 'registration.html', context)


# user login

def login(request):
    form = loginform()
    if request.method == 'POST':
        form = loginform(data=request.POST)
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if form.is_valid():
            if user is not None:
                auth_login(request, user)
                print("loginned")
                messages.success(request, "Loginned")
                return redirect('userhome')
            else:
                messages.error(request, "form not  saved")
        else:
            form = loginform()
    context = {'form': form}
    return render(request, 'login.html', context)


# user Logout

def logout_user(request):
    logout(request)
    return redirect("home")


# users page after logined


def userhome(request):
    tasks = Todo.objects.filter(user_id=request.user.id)
    context = {
        'tasks': tasks
    }
    return render(request, 'userhome.html', context)


# adding tasks


def Addtask(request):
    addform = TodoForm()
    if request.method == 'POST':
        addform = TodoForm(data=request.POST)
        if addform.is_valid():
            task=request.POST.get('task')
            time=request.POST.get('time')
            add=Todo.objects.create(task=task,time=time)
            add.user=(request.user)
            add.save()
            print("task added")
            messages.info(request, "task added")
            return redirect("userhome")
        else:
            print("not added")
    context = {
        'addform': addform
    }
    return render(request, 'addtask.html', context)

# edit tasks


def edittask(request, id):
    Edittask = Todo.objects.get(id=id)
    form = taskeditform(instance=Edittask)
    if request.method == "POST":
        form = taskeditform(data=request.POST, instance=Edittask)
        if form.is_valid():
            form.save()
            print("edited")
            messages.info(request, "task edited")
            return redirect('userhome')
        else:
            print("not edited")
    context = {'form': form, 'id': id}
    return render(request, "taskedit.html", context)


# delete tasks


def Deletetask(request, id):
    taskdelete = Todo.objects.get(id=id)
    taskdelete.delete()
    messages.error(request, "deleted")
    return redirect('userhome')
