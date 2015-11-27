from django.contrib.auth import authenticate,login,logout
from django.shortcuts import render, HttpResponse,redirect
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from application.models import menu, orderplaced , verification
from datetime import date, timedelta
import time

def changestatus(request):
    if request.method == "POST":
        incoming_dict = request.POST
        order_number = incoming_dict.get('order_id')
        order_status = incoming_dict.get('order_status')

        orderplaced.objects.filter(order_id =order_number).update(status = order_status)
        print "Saved"
        return HttpResponse("Yo mofo")
    else:
        return render(request,"changestatus.html")



def verification(request):
    if request.method == "POST":
        incoming_dict = request.POST
        username = incoming_dict.get('username')
        verification_number =incoming_dict.get('verification')
        try:
            print "coming here"
            obj = User.objects.filter(username = username).update(is_active= True)
            print obj
            return redirect('/')
        except:
            print "Entering here"
            return redirect('/verification/')

    else:
        return render(request,'verification.html')






def LiveTracking(request):
    if request.method == "POST":
        incoming_dict = request.POST
        order_no = incoming_dict.get('order_number')
        img = ""
        try:
            order_status = orderplaced.objects.get(order_id = order_no).status
            username = orderplaced.objects.get(order_id = order_no).username
            placed_on = orderplaced.objects.get(order_id = order_no).placed_on
            order_id = orderplaced.objects.get(order_id = order_no).order_id


            return render(request,'livetracking/index.html',{'order_status' : order_status,'order_id' : order_id, 'username' : username , 'placed_on' : placed_on})
        except:
            print "error"


    else:
        return render(request, "livetracking.html")
    return HttpResponse("Live tracking over here bitch")


#20151126223505


def Load_Menu(request, **kwargs):
    if request.user.is_authenticated():
        rest_name = kwargs.get('menu_name')
        try:
            items = menu.objects.filter(rest_name = rest_name)
            list = []
        except:
            pass
        for x in items:
            only_dish = str(x)
            list.append(only_dish)
        print list

        return render(request,'load_menu.html',{'list' : list})

    else:
        return redirect('/signin')

def PlaceOrder(request):

    if request.method == "POST":
        incoming_dict = request.POST
        order = ""
        for x in incoming_dict.get('dishes'):
            order = order + x
        print incoming_dict.get('dishes')
        message = "Order Has been placed" + "Order is                 " + order
        print message
        username = request.user
        date_token = str(date.today())
        current_time =  str(time.strftime("%H:%M:%S"))
        order_id = ""
        for x in date_token:
            if x is "-":
                pass
            else:
                order_id = order_id + x

        for x in current_time:
            if x is ":":
                pass
            else:
                order_id = order_id + x


        print "%%%"*10
        name = str(request.user)
        print name
        print orderplaced.objects.all()
        new_order = orderplaced.objects.create(username=name,order = order, order_id = order_id)
        print orderplaced.objects.all()


        send_mail("Incoming Order " , message, 'foodsquare10@gmail.com', ['foodsquare10@gmail.com'])
        #send_mail("Thanks For Ordering" , "Dear " +  request.user + " Your food will reach you shortly!", "foodsquare10@gmail.com", [])


    return HttpResponse(order_id)



def Profile(request):
    return redirect('/')


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
                    return HttpResponse("Unverified account")
            else:
                return HttpResponse("Unverified")

        except:
            return HttpResponse("Invalid email/password")
    return render(request, 'SignIn.html')


def Register(request):

    if request.method=='POST':



        user_registered = False
        detail = request.POST
        email = detail.get('email')
        email_domain_check = email.split('@')
        new_password = ""
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

                    new_passsword = make_password(password=password,salt=None,hasher='unsalted_md5')
                    user = User.objects.create_user(username=username,email = email, password = new_password)
                    user.is_active = False
                    user.save()
                    #send_mail("One time registering" , "Dear " +  username + "OTP is : 45654345 "   , "foodsquare10@gmail.com", [email])
                    return HttpResponse("SUCCESS kindly proceed with log in")
                except:
                    return HttpResponse("Username already in use")
            else:
                return HttpResponse("Sorry you are already registered with email id : " + email)
        else:
            return HttpResponse("Sorry the facilities of FoodSquare are only limited to Students and faculty members of NIIT University")
    else:
        return render(request,'register.html')

    return render(request,'register.html')




def Restaurant_Menu(request):
    return render(request,'menu/index.html')

