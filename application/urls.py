from django.conf.urls import url
from application import views

urlpatterns = [

    url(r'^$', views.WelcomePage),
    url(r'^contact_us', views.ContactUs),
    url(r'^signin', views.SignIn),
]