from django.urls import path
from .import views

urlpatterns = [
    path("newone",views.welcome,name='newone'),
    path('log in',views.loginpagedef,name='log_in'),
    path('home page',views.homepagedef,name='home_page')
]