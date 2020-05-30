from django.shortcuts import render
from .models import Image
# Create your views here.
def home(request):
    return render(request,'ista/index.html')

def about(request) :
    return HttpResponse("<h1>About page</p>")
   