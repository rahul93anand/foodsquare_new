from django.conf.urls import url
from application import views

urlpatterns = [

    url(r'^$', views.WelcomePage),
    url(r'^contact_us', views.ContactUs),
    url(r'^signin', views.SignIn),
    url(r'^register', views.Register),
    url(r'^rest_menu', views.Restaurant_Menu),
    url(r'^load_menu/(?P<menu_name>[\w-]+)$', views.Load_Menu),
    url(r'^placeorder/', views.PlaceOrder),

]