from django.contrib.auth.hashers import make_password, check_password
from django.shortcuts import render, redirect

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
    returnPage = 'login.html'

    if request.method == 'GET':
        return render(request,returnPage)

    elif request.method == 'POST':
        form = request.POST.dict()

        error=''
        if not (form['userid'] and form['password']):
            error = '입력 오류'
        else:
            try:
                member = Member.objects.get(userid=form['userid'])
            except Member.DoesNotExist:
                member = None

            if member and check_password(form['password'],member.passwd):
                request.session['userid']=form['userid']

                return redirect('/')
            else:
                error = '아이디나 비밀번호가 틀립니다.'

        context={'error':error}

        return render(request,returnPage,context)

def myinfo(request):
    member={}


    if request.session.get('userid'):
        userid = request.session.get('userid')
        member=Member.objects.get(userid=userid)

    context={'member':member}
    return render(request, 'myinfo.html',context)


def logout(request):
    if request.session.get('userid'):
        del(request.session['userid'])

    return redirect('/')