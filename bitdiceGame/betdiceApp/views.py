from django.shortcuts import render
import json,random
def index(request):
    return render(request,'index.html',{})

def bet(request):
    betnumber = request.POST['betnumber']
    randomnumber = random.randint(0,100)
    if(int(betnumber)<randomnumber):
        youwin = "You Win!"
    else:
        youwin = "You Lose!"
    mydict = {'betnumber' : betnumber,
            'randomnumber': randomnumber,
            'youwin':youwin}
    return render(request,'bet.html',mydict)
             
# Create your views here.
