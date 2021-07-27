from django.shortcuts import render,HttpResponse
from .forms import userform , depo
from .models import user


def bankuser(request):
    if request.method == 'POST':
        fm = userform(request.POST)
        if fm.is_valid():
            fm.save()
        fm=userform()
    else:
        fm=userform()
    return render(request,'bank/log.html',{'form':fm})


def deposit(request):
    if request.method == 'POST':
        df=depo(request.POST)
        all=user.objects.all()
        if df.is_valid():
            for i in all:
                if i.name == df.cleaned_data['depo_by']:
                    i.amount_add-=df.cleaned_data['depo_amt']
                    i.save()

                    break
                    #print('name:',df.cleaned_data['name1'])
                    #print('amount:',df.cleaned_data['depo_mony'])
                    #print(i.name)
                    #print(i.amount_add)
            else:
                return HttpResponse('<h1>USER IS NOT PRESENT</h1>')
            for i in all:
                if i.name == df.cleaned_data['depo_to']:
                    i.amount_add+=df.cleaned_data['depo_amt']
                    i.save()
                    break
        df=depo()
    else:
        df=depo()
    return render(request,'bank/deposit.html',{'depo':df})

# Create your views here.
