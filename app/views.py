from django.shortcuts import render

# Create your views here.

def nested(request):
    d={'a':200,'b':500,'c':300,'d':400}
    return render(request,'nested.html',d)
