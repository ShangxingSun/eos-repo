import subprocess
from django.shortcuts import render
import json,random
from subprocess import PIPE
from shlex import split


def index(request):
    return render(request,'index.html',{})

def bet(request):
    betnumber = request.POST['betnumber']
    cleosAlisa = 'sudo docker exec -it eosio /opt/eosio/bin/cleos --url http://127.0.0.1:7777 --wallet-url http://127.0.0.1:5555'
    command = cleosAlisa + " push action getnumber hi \'[\"getnumber\"]\' -p getnumber@active"
    try:
        out_bytes = subprocess.check_output(split(command))
    except subprocess.CalledProcessError as e:
        out_bytes = e.output       # Output generated before error
        code      = e.returncode   # Return code
        print(out_bytes)
        print(code)
    outnumber = out_bytes.decode('utf-8')
    randomnumber = int(outnumber[outnumber.find('>>')+3:outnumber.find('>>')+5])
    print(randomnumber)
    if(int(betnumber)<randomnumber):
        youwin = "You Win!"
    else:
        youwin = "You Lose!"
    mydict = {'betnumber' : betnumber,
            'randomnumber': randomnumber,
            'youwin':youwin}
    return render(request,'bet.html',mydict)
             
# Create your views here.
