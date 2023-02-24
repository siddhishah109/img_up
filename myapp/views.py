from django.shortcuts import render
from .forms import imageform
from .models import image

# Create your views here.
def home(request):
    if request.method =='POST':
        form =imageform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    form= imageform()
    img=image.objects.all()
    return render(request,'home.html',{'form':form,'img':img})
