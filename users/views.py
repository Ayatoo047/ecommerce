from django.template.loader import get_template
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.http import HttpResponse
import random
from .models import *
from django.conf import settings
from pytz import timezone
import datetime

# Create your views here.

def generateOtp():
    genotp = [random.randint(0,9) for number in range(6)]
    otp = ("".join([str(i) for i in genotp]))
    return(otp)


def loginUser(request):

    page = 'login'
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.object.get(username=username)

        except:
            HttpResponse('user doesnt exist')

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
        otp=generateOtp()
        username = request.POST['username'].lower()
        password = request.POST['password']
        email = request.POST['email']
        confirmpassword = request.POST['confirmpassword']
        
        if password != confirmpassword:
            print('password doesnt match')

        user = User.objects.create_user(
            username = username,
            password = password,
            email=email,
            # password2 = confirmpassword,
        )
        user.is_active = False
        login(request, user)

        profile = Profile.objects.create(
            user = request.user,
        )
        Otp.objects.create(
            otp = otp,
            profile = profile
        )
        sendEmail(request, otp=otp)
        return redirect('otpverification')

    
    return render(request, 'users/login-register.html')

def sendEmail(request, otp):
    mail_subject = 'Trascation File'
    message = render_to_string('otpemail.html', {
        'otp': otp,
    })
    to_email = [request.user.email]
    context_dict = {
        'user': request.user.profile.first_name,
        'otp': otp,
        'to_email' : to_email
    }
    template = get_template('otpemail.html')
    message  = template.render(context_dict)
    
    
    email = EmailMultiAlternatives(
        subject=mail_subject,
        body='This is your document',
        from_email =settings.EMAIL_HOST_USER,
        to = [to_email]
    )
    email.attach_alternative(message, "text/html")
 
    email.send(fail_silently=True)
    render(request,template_name='users/otp-verification.html')
    print('success', otp)

def verifyOtp(request):
    profile = request.user.profile
    otp = Otp.objects.filter(profile__id=profile.id).first()
    if request.method == 'POST':
        userotp = request.POST['inputotp']

        now = timezone('UTC').localize(datetime.datetime.now())
        created_time = otp.created + datetime.timedelta(hours = 1)
        if userotp == str(otp):
            if (now - created_time) >= datetime.timedelta(minutes = 1):
                print('otp expired, new sent')
                otp.otp = generateOtp()
                otp.save()
                newotp = otp.otp
                sendEmail(request, otp=str(newotp))
                return redirect('otpverification')


            elif (now - created_time) < datetime.timedelta(minutes = 1):
                otp.otp = '-'
                otp.save()




                return redirect('index')

    context = {'profile': profile, 'otp':otp}
    return render(request, 'users/otp-verification.html', context)



def logoutuser(request):
    logout(request)
    return redirect('index')


def adminpanel(request):
    user = request.user
    if user.is_superuser == False:
        HttpResponse('You are not allowed')

    context = {'user': user}
    return render(request, 'admin.html', context)