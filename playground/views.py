from django.shortcuts import render
from django.http import HttpResponse
import imaplib
#views are request handlers
# Create your views here.



def calculate():
    x = 1
    y = 2
    return x

def say_hello(request):
    x = calculate()
    y = 2
    return render(request,'hello.html', {'msg': 'This is a dummy message kindly ignore it'})