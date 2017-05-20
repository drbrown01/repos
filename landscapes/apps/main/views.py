from django.shortcuts import render
from . import models
import random

# Create your views here.
#this function is to determine is Prime number or not, for use on urls
def isPrime(n):
    n = int(n)
    i = 2
    while(i * i <= n ):
        if(n % i == 0):
            return False
            i += 1
    return n > 1


def index(request, n):
    n = int(n)
    landscapes = [
        'https://static.pexels.com/photos/70589/pexels-photo-70589.jpeg',
        'http://weknownyourdreamz.com/images/jungle/jungle-02.jpg',
        'http://wallpaper-gallery.net/images/desert-images/desert-images-6.jpg',
        'http://anguerde.com/pics/main/53/394507-vineyard.jpg',
        'http://cdn.wccftech.com/wp-content/uploads/2016/09/spacee-1920x1200.jpg',
        'https://wallpaperscraft.com/download/planet_light_spots_space_86643/1920x1080#',
        ]
    if n <1 or n >50:
        pic = random.choice(landscapes)
    elif isPrime(n):
        pic = landscapes[-1]
    elif n < 11:
        pic = landscapes[0]
    elif n < 21:
        pic = landscapes[1]
    elif n < 31:
        pic = lanscapes[2]
    elif n < 41:
        pic = lanscapes[3]
    else:
        pic = landscapes[4]
    context = {
        'pic': pic,
    }



    return render(request, 'main/index.html', context)
