from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User

# Create your views here.
def loginUser(request):

    page = 'login'
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.object.get(username=username)

        except:
            print('user doesnt exist')

        user = authenticate(username = username, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            print('something went wrong')

    context = {'page': page}
    return render(request, 'users/login-register.html', context)

def registerUser(request):
    user = None

    if request.method == "POST":
        username = request.POST['username'].lower()
        password = request.POST['password']
        confirmpassword = request.POST['confirmpassword']
        
        if password != confirmpassword:
            print('password doesnt match')

        user = User.objects.create_user(
            username = username,
            password = password,
            # password2 = confirmpassword,
        )
        user.save()
        login(request, user)
        return redirect('index')
    
    return render(request, 'users/login-register.html')


        

def logoutuser(request):
    user = request.user
    if request.method == 'POST':
        logout(request, user)
