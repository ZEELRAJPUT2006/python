from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import razorpay
from django.conf import settings
from django.core.mail import send_mail
import requests

# Create your views here.
def index(request):
    return render(request,'index.html')

def payment(request):
    amt = request.GET['amt']
    client = razorpay.Client(auth=("rzp_test_S1Hsg7YN8MlwDU", "ZKs1rK1XnjRDNd4uxjP2NcRJ"))

    
    data = { "amount": int(amt)*100, "currency": "INR", "receipt": "order_rcptid_11" }
    payment = client.order.create(data=data) # Amount is in currency subunits.
    
    return JsonResponse(payment)


def sendmail(request):
    context = {}
  
    if request.method == 'POST':
        address = request.POST.get('address')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        if address and subject and message:
            try:
                send_mail(subject, message, settings.EMAIL_HOST_USER, [address])
                context['result'] = 'Email sent successfully'
            except Exception as e:
                context['result'] = f'Error sending email: {e}'
        else:
            context['result'] = 'All fields are required'
    
    return render(request,"mail.html",context)

def sendsms(request):
    import requests
    from django.http import HttpResponse

    url = "https://www.fast2sms.com/dev/bulkV2"

    headers = {
        "authorization": "ysrMfRaXC6PqSUE4m8ncI51D0ouvTYNdhk3QOVBLjzbiZ92Kpw3t9ORqxJ1k0fy4MNgQjKhcFAsbDpHi",
        "Content-Type": "application/x-www-form-urlencoded",
        "cache-control": "no-cache"
    }

    payload = {
        "route": "q",
        "message": "This is test message",
        "language": "english",
        "numbers": "8866280999"
    }

    response = requests.post(url, data=payload, headers=headers)
    return HttpResponse(response.text)
