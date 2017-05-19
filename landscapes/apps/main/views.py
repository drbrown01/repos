from django.shortcuts import render
from . import models

# Create your views here.
def isPrime(n):
    n = int(n)
    i = 2
    while(i * i <= n ):
        if(i % n == 0):
            return False
            i += 1
    return n > 1


def index(request, n):
    n = int(n)
    print isPrime(n)
    return render(request, 'main/index.html')
