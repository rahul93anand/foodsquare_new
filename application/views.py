from django.contrib.auth import authenticate,login,logout
from django.shortcuts import render, HttpResponse
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from application.models import menu





def Load_Menu(request, **kwargs):
    rest_name = kwargs.get('menu_name')
    try:
        items = menu.objects.filter(rest_name = rest_name)
        dict = {'food_list' : items}
        print dict
    except:
        pass

    return render(request,'load_menu.html',items)


def WelcomePage(request):
    try:
        print User.objects.all()
    except:
        pass
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
                    return HttpResponse("Hey your account is disabled")
            else:
                return HttpResponse("Invalid Id/Password")
        except:
            return HttpResponse("Invalid email/password")
    return render(request, 'SignIn.html')


def Register(request):
    return render(request,'register.html')




def Restaurant_Menu(request):
    return render(request,'menu/index.html')



