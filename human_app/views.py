from human_app.skintone import imageskintone
from django.shortcuts import render
from matplotlib import image
from .forms import ImageForm
from human_app.models import Image, Questions
from . import skintone
from . import models

# Create your views here.
def index(request):
    visit = "disabled"
    return render(request,"index.html",{"visit1":visit})

def skintone(request):
    visit = "skintone"
    return render(request,"skintone.html",{"visit2":visit})


def about(request):
    visit = "about"
    return render(request,"about.html",{"visit3":visit})


def contact(request):
    visit = "contact"
    return render(request,"contact.html",{"visit4":visit})


def capture(request):
    visit = "capture"
    return render(request,"capture.html",{"visit5":visit})


def help(request):
        visit = "contact"
        if request.method=="POST":
            values = Questions()
            
            values.name = request.POST['name'] 
            values.email = request.POST['email'] 
            values.ques = request.POST['question'] 
            values.detail = request.POST['subject'] 
            # singin.save()
            result = values.name
            values.save()
            
            return render(request,"contact.html",{"yourname":result,"visit4":visit})

        else:
            return render(request,"contact.html",{"visit4":visit})       
            


def capturedimage(request):
    visit = "capture"
    if request.method == "POST":
        imgdata = request.POST['captureimagedata']
        if imgdata :
            skin_tones = imageskintone(imgdata)
            
            return render(request,"capture.html",{"snapdata":skin_tones,"visit5":visit})

        else:
            captureinvalid = "captureinvalid"
            return render(request,"capture.html",{"captureinvalid":captureinvalid,"visit5":visit})

    else:
        return render(request,"capture.html")            


def SaveImage(request):
    visit = "skintone"
    if request.method == "POST":
        form=ImageForm(data=request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            obj=form.instance

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
            if obj :            
                imag =  obj.image
                url = "http://127.0.0.1:8000/media/" + str(imag)
                skin_tones = imageskintone(url)
                form = ImageForm()
                
                return render(request,"skintone.html",{"obj":obj,"skinto":skin_tones,"visit2":visit})
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                      
    else:
        return render(request,"skintone.html",{"visit2":visit})

    


