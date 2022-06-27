from django.shortcuts import render, redirect

# Create your views here.
from django.views.decorators.cache import cache_control

from board.models import Board
from member.models import Member

@cache_control(no_cache=True,no_store=True,must_revalidate=True)
def list(request):
    # bdlist=Board.objects.values('id','title','userid','regdate','views').order_by('-regdate')
    bdlist=Board.objects.select_related('member')
    # bdlist.get(0).member.userid

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
                                      member=Member.objects.get(pk=form['memberid'])
                                      )
            board.save()

            return redirect('/list')


    context = {'form':form,'error': error}
    return render(request, returnPage,context)



def view(request):
    if request.method == 'GET':
        form = request.GET.dict()

        # b = Board.objects.get(id=form['bno'])
        # b.views += 1
        # b.save()
        from django.db.models import F
        Board.objects.filter(id=form['bno']).update(views=F('views')+1)

        bd = Board.objects.select_related('member').get(id=form['bno'])
    # print(form['bno'])
    elif request.method == 'POST':
        pass

    context={'bd':bd}

    return render(request, 'view.html',context)


def remove(request):
    if request.method == 'GET':
        form=request.GET.dict()
        Board.objects.filter(id=form['bno']).delete()
    return redirect('/list')


def modify(request):
    if request.method == 'GET':
        form=request.GET.dict()
        bd = Board.objects.get(id=form['bno'])
    elif request.method == 'POST':
        form=request.POST.dict()
        # b= Board.objects.get(id=form['bno'])
        # b.title=form['title']
        # b.contents=form['contents']
        # b.save()

        Board.objects.filter(id=form['bno']).update(title=form['title'],contents=form['article'])

        return redirect('/view?bno='+ form['bno'])

    context = {'bd':bd}
    return render(request,'modify.html',context)
