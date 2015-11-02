
from django.shortcuts import render, HttpResponse
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

def WelcomePage(request):
    return render(request,"index.html")

def ContactUs(request):
    if request.method == "POST":

        detail = request.POST
        name = detail.get("name")
        email = detail.get("email")
        message = detail.get("message") + "    EMAIL ID :  " + email
        send_mail("Hey We got a message from " + name, message, 'foodsquare10@gmail.com', ['foodsquare10@gmail.com'])
        send_mail("Thanks For sharing" , "Dear " +  name + " thanks for sharing valuable feedback with us, our team will get back to you shortly xD", "foodsquare10@gmail.com", [email])
        return render(request,"index.html",{'status' : "Message sent"})


def SignIn(request):
    if request.method =="POST":
        print("Hello")
    return render(request, 'SignIn.html')


def Register(request):
    if request.method=='POST':
        detail = request.POST
        email = detail.get('email')
        username = detail.get('username')
        password = detail.get('password')
        print(request.POST)
        user = User.objects.create_user(username=username)
        user.email= email
        user.password = make_password(password=password,salt=None,hasher='unsalted_md5')
        user.save()
        send_mail("Thanks For registering" , "Dear " +  username + " thanks for registering with foodsquare xD", "foodsquare10@gmail.com", [email])



    return render(request,'register.html')


# Create your views here.


# Create your views here.
