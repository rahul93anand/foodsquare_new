
from django.shortcuts import render, HttpResponse
from django.core.mail import send_mail

def WelcomePage(request):
    return render(request,"index.html")

def ContactUs(request):
    if request.method == "POST":
        detail = request.POST
        name = detail.get("name")
        email = detail.get("email")
        message = detail.get("message")
        send_mail("Hey We got a message from " + name, message, 'foodsquare10@gmail.com', ['foodsquare10@gmail.com'])
        
        return render(request,"index.html",{'status' : "Message sent"})


def SignIn(request):
    if request.method =="POST":
        print(request.POST)

    return render(request, 'SignIn.html')


# Create your views here.


# Create your views here.
