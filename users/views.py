from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User

# Create your views here.
def loginUser(request):
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

    context = {}
    return render(request, 'users/login-register.html', context)
