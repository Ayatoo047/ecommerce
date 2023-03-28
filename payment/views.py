from django.shortcuts import get_object_or_404, render, redirect
from django.http.request import HttpRequest
from django.http.response import HttpResponse

from django.contrib import messages
from django.conf import settings

from products.models import Cart
from .models import Payment
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa



# def checkout(request):
#     profile = request.user.profile
#     if request.user.is_authenticated:
#         cart, created = Cart.objects.get_or_create(owner=request.user.profile)
#         cartitems = cart.cartitems.all()
    
#     context = {'cart': cart, 'items': cartitems, 'profile': profile}
#     return render(request, 'payment/checkout.html', context)


def thankyou(request):
    return render(request, 'products/thankyou.html')

def initiate_payment(request: HttpRequest) -> HttpResponse:
    profile = request.user.profile
    cart = Cart.objects.select_related('owner').filter(owner__id=request.user.profile.id).first()
    # cart, created = Cart.objects.get_or_create(owner=request.user.profile)
    cartitems = cart.cartitems.all()
    if request.method == "POST":
        print(cart)
        email = request.user.email
        amount = cart.grandtotal
        orderitems = cart.cartitems.all()

        pay = Payment.objects.create(name=profile,email=email,amount=amount,) #fee_type=fee_type,state_ID=state_ID
        # pays = Payment.objects.get(ref=pay.ref)
        return render(request, 'payment/reciept1.html', {'payment': pay, 'paystack_public_keY': settings.PAYSTACK_PUBLIC_KEY})
    context = {'cart': cart, 'items': cartitems, 'profile': profile}
    return render(request, 'payment/checkout.html', context)

def verify_payment(request, ref: str):
    trxref = request.GET["trxref"]
    if trxref != ref:
        messages.error(
            request,
            "The transaction reference passed was different from the actual reference. Please do not modify data during transactions",
        )
    payment: Payment = get_object_or_404(Payment, ref=ref)
    
    if payment.verify_payment():
        messages.success(
            request, f"Payment Completed Successfully, NGN #{payment.amount}."
        )

        template = get_template('invoice.html')
        data = {
            'order_id': payment.ref,
            'STATE_ID': payment.state_ID,
            'user_email': request.user.email,
            'date': str(payment.date_created),
            'name': payment.name,
            'fee': payment.fee_type,
            'amount': payment.amount,
        }
        html  = template.render(data)
        result = BytesIO()
        pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result), #link_callback=fetch_resources)
        pdf = result.getvalue()
        filename = 'Value_' + data['fee'] + '.pdf'

        mail_subject = 'Trascation File'
        message = render_to_string('emailinvoice.html', {
            'orderid': payment.ref,
             'name': payment.name,
            'fee': payment.fee_type,
            'amount': payment.amount,
            'stateid' : payment.state_ID,
        })
        to_email = ['government1.irs@gmail.com', request.user.email]
        context_dict = {
            'user': request.user.profile.full_name,
            'orderid': payment.ref,
            'amount': payment.amount,
            'fee': payment.fee_type,
            'stateid' : payment.state_ID,
            'to_email' : to_email
        }
        template = get_template('emailinvoice.html')
        message  = template.render(context_dict)
        

        # I use this loop because I dont want the two parties to see each other's email
        for email in to_email:
            email = EmailMultiAlternatives(
                subject=mail_subject,
                body='This is your document',
                from_email =settings.EMAIL_HOST_USER,
                to = [email]
            )
            email.attach_alternative(message, "text/html")
            email.attach(filename, pdf, 'application/pdf')
            email.send(fail_silently=False)
            print('success')
  
    else:
        messages.warning(request, "Sorry, your payment could not be confirmed.")
    return render(request,)