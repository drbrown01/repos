from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    return render(request, 'main/index.html')

def create(request):

    print request.POST
    return redirect('/')
