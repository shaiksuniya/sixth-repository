from django.shortcuts import render

# Create your views here.
def conditions(request):
    d={'a':6200,'b':3000,'c':4000}
    return render(request,'conditions.html',context=d)


def loops(request):
    d={'name':'SHAIK SONU'}
    return render(request,'loops.html',d)