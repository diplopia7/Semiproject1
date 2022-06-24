from django.shortcuts import render, redirect

# Create your views here.
from board.models import Board
from member.models import Member


def list(request):
    bdlist=Board.objects.values('id','title','userid','regdate','views').order_by('-regdate')

    context={'bds':bdlist}

    return render(request, 'list.html',context)


def write(request):
    returnPage='write.html'
    form=''
    error=''

    if request.method == 'GET':
        pass
    elif request.method == 'POST':
        form = request.POST.dict()

        if not (form['title'] and form['article']):
            error = '입력 오류'
        else:
            board = Board(title=form['title'],contents=form['article'],
                                      userid=Member.objects.get(pk=form['memberid'])
                                      )
            board.save()

            return redirect('/list')


    context = {'form':form,'error': error}
    return render(request, returnPage,context)


def view(request):
    return render(request, 'view.html')