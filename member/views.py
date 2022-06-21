from django.shortcuts import render


# Create your views here.
def join(request):
    return render(request, 'join.html')


def login(request):
    return render(request, 'login.html')

def myinfo(request):
    return render(request, 'myinfo.html')
