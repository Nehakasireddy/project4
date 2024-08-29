from django.shortcuts import render

# Create your views here.
def conditions(request):
    d={'a':400,'b':200,'c':500}
    return render(request,'conditions.html',context=d)

def loop(request):
    d={'name':'Neha','mobile':[12345,56789]}
    return render(request,'loop.html',context=d)
