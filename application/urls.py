from django.conf.urls import url
from application import views

urlpatterns = [

    url(r'^$', views.WelcomePage),
    url(r'^contact_us', views.ContactUs),
    url(r'^signin', views.SignIn),
    url(r'^register', views.Register),
    url(r'^rest_menu', views.Restaurant_Menu),
    url(r'^load_menu/(?P<menu_name>[\w-]+)$', views.Load_Menu),
<<<<<<< HEAD
    url(r'^placeorder/', views.PlaceOrder),
=======
>>>>>>> 5cb727255ffb1bbda89b4243baf35058d2ab7ead

]