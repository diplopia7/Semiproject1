from django.contrib.auth.hashers import make_password
from django.shortcuts import render


# Create your views here.
from member.models import Member


def join(request):
    returnPage='join.html'

    if request.method=='GET':
        return render(request, returnPage)
    elif request.method=='POST':
        form = request.POST.dict()
        # print(form,form['id'])
        error = ''
        if not (form['id'] and form['password'] and form['check_password'] and form['name'] and form['email']):
            error='입력값이 누락되었습니다.'
        elif form['password']!=form['check_password']:
            error='비밀번호가 일치하지 않습니다.'
        else:
            member = Member(
                userid=form['id'],
                passwd=make_password(form['password']),
                name=form['name'],
                email=form['email']
            )
            member.save()

            returnPage='joinok.html'

        context={'form':form,'error':error}

        return render(request, returnPage,context)


def login(request):
    return render(request, 'login.html')

def myinfo(request):
    return render(request, 'myinfo.html')
