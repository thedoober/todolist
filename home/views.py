from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from home.models import todo
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def index(request):
#   if request.user.is_authenticated:
    if request.method=="POST":
        task =request.POST.get('task')
        if len(task) <  3:
            messages.error(request, "Please write some thing meaningful")
            return redirect('home')
        else:
            
            new_todo = todo(user=request.user, todo_name=task)
            new_todo.save()

    all_todos =todo.objects.filter(user=request.user) 
    context ={
        "user": request.user.username,
        'todos' : all_todos
    }   
    return render(request,"index.html", context)
#   else:
#       return redirect("/login")
def register(request):
    if request.user.is_authenticated:
        return redirect("home")
    if request.method == "POST":
        name = request.POST.get("name").lower()
        email = request.POST.get("email")
        password = request.POST.get("password")

        
        if len(password)<5:
            messages.warning(request, "password length is less than 5")
            return redirect("/register")
        
        get_user = User.objects.filter(email =email)
        if get_user:
            messages.warning(request, "user already exists")
            return redirect("login")

        
        new_user = User.objects.create_user(username= name, email=email, password=password)
        new_user.save()
        messages.success(request, "User successfully created, login now")
        return redirect("/login")
    return render(request,"register.html")
  
def userlogin(request):
    if request.user.is_authenticated:
        return redirect("home")
    if request.method == "POST":
        name = request.POST.get("name").lower()

        # usernam = User.objects.get(email=email.lower()).username
        password = request.POST.get("password")
        user = authenticate(username=name, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            messages.warning(request, "Error, wrong user details or user not exists")
            return redirect("login")
           
    return render(request,"login.html")

def userlogout(request):
    logout(request)
    return redirect("login")
def tododelete(request, name):
    print(request)
    get_todo = todo.objects.get(user= request.user, todo_name=name)
    get_todo.delete()
    return redirect('home')
    
    
def todoupdate(request, name):
    if not name:
        return HttpResponse("Wrong Input")

    get_todo = todo.objects.get(user= request.user, todo_name=name)
    get_todo.status = True
    get_todo.save()
    return redirect('home')

   



   





