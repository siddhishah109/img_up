from django.shortcuts import render
from .forms import imageform
from .models import image

# Create your views here.
def home(request):
    form=imageform()
    return render(request,'home.html',{'form':form})
