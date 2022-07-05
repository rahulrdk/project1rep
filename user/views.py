from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def welcome(request):
    return HttpResponse("hello")


def loginpagedef(request):
    return render(request,'user/login.html')

def homepagedef(request):
    return render(request,'user/home.html')