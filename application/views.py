from django.contrib.auth import authenticate,login,logout
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
        detail = request.POST
        email = detail.get('email')
        password = detail.get('password')
        try:
            username = User.objects.get(email=email)
            user = authenticate(username=username,password=password)
            if user:
                if user.is_active:
                    login(request, user)
                    return HttpResponse("yo signed in")
                else:
                    return HttpResponse("Hey you fuckface your account is disabled")
            else:
                return HttpResponse("Invalid Id/Password")
        except:
            return HttpResponse("Invalid email/password")
    return render(request, 'SignIn.html')


def Register(request):
    if request.method=='POST':
        user_registered = False
        detail = request.POST
        email = detail.get('email')
        email_domain_check = email.split('@')
        if email_domain_check[1] == 'st.niituniversity.in' or email_domain_check[1] == 'niituniversity.in':
            try:
                User.objects.get(email=email)
                user_registered = True
            except:
                pass


            if not user_registered:
                username = detail.get('username')
                password = detail.get('password')
                print(request.POST)
                try:
                    user = User.objects.create_user(username=username)
                    user.email= email
                    user.password = make_password(password=password,salt=None,hasher='unsalted_md5')
                    user.save()
                    send_mail("Thanks For registering" , "Dear " +  username + " thanks for registering with foodsquare xD", "foodsquare10@gmail.com", [email])
                    return HttpResponse("SUCCESS kindly proceed with log in")
                except:
                    return HttpResponse("Username already in use")
            else:
                return HttpResponse("Sorry you are already registered with email id : " + email)
        else:
            return HttpResponse("Sorry the facilities of FoodSquare are only limited to Students and faculty members of NIIT University")
    else:
        return render(request,'register.html')





