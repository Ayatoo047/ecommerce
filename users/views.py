from io import BytesIO
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
import random
from .models import *
from django.conf import settings

# Create your views here.

def generateOtp():
    genotp = [random.randint(0,9) for number in range(6)]
    otp = ("".join([str(i) for i in genotp]))
    return(otp)
    # email = input("input your email: ")
    # confirmation_test = False

    # while confirmation_test is False:
        # otp.append(random.randint(0, 9))
    
        # confirmation = input("input otp: ")
        # if confirmation != join:
        #     print("wrong otp")
        # elif confirmation == join:
        #     confirmation_test = True
        #     print("welcome", email)


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


# from xhtml2pdf import pisa
from django.template.loader import get_template
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives


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

        Profile.objects.create(
            user = request.user,
            otp = otp
        )
        # verifyOtp(request, otp=otp)
        sendEmail(request, otp=otp)
        return redirect('otpverification')

        # return redirect('index')
    
    return render(request, 'users/login-register.html')

def sendEmail(request, otp):
    # template = get_template('invoice.html')
    # data = {
    #     'otp': generateOtp(),
    #     'name'
    # }
    # html  = template.render(data)
    # result = BytesIO()
    # pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result), #link_callback=fetch_resources)
    # pdf = result.getvalue()
    # filename = 'Value_' + data['fee'] + '.pdf'

    mail_subject = 'Trascation File'
    message = render_to_string('otpemail.html', {
        'otp': otp,
        # 'name': payment.name,
        # 'fee': payment.fee_type,
        # 'amount': payment.amount,
        # 'stateid' : payment.state_ID,
    })
    to_email = [request.user.email]
    context_dict = {
        'user': request.user.profile.first_name,
        'otp': otp,
        # 'amount': payment.amount,
        # 'fee': payment.fee_type,
        # 'stateid' : payment.state_ID,
        'to_email' : to_email
    }
    template = get_template('otpemail.html')
    message  = template.render(context_dict)
    

    # I use this loop because I dont want the two parties to see each other's email
    
    email = EmailMultiAlternatives(
        subject=mail_subject,
        body='This is your document',
        from_email =settings.EMAIL_HOST_USER,
        to = [to_email]
    )
    email.attach_alternative(message, "text/html")
        # email.attach(filename, pdf, 'application/pdf')
    email.send(fail_silently=False)
    render(request,template_name='users/otp-verification.html')
    print('success', otp)
    # return (request, 'users/otp-verification.html')
    # user = request.user
    # if request.method == 'POST':
    #     userotp = request.POST['inputotp']
    #     if userotp == otp:
    #         login(request, user)
    #         return redirect('index')

    # else:
    #     messages.warning(request, "Sorry, your payment could not be confirmed.")
def verifyOtp(request):
    # user = request.user
    profile = request.user.profile
    if request.method == 'POST':
        userotp = request.POST['inputotp']
        if userotp == profile.otp:
            # login(request, user)
            # profile.otp.delete()
            return redirect('index')

    context = {'profile': profile}
    return render(request, 'users/otp-verification.html', context)


        

def logoutuser(request):
    user = request.user
    if request.method == 'POST':
        logout(request, user)
