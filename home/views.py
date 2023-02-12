from .demo import test_calendar
from django.shortcuts import render,redirect
from django.views.generic.base import TemplateView,RedirectView,View
from .forms import UserCreationForm,UserLoginForm,PasswordChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login,logout,authenticate,update_session_auth_hash
from django.http import JsonResponse,HttpResponse
from .chatbot.chatbot import message as MessageChatBot
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json
import os
from zipfile import ZipFile
from io import BytesIO
from .assessment.assess import assessment
from .models import UploadedFile
import cv2
import pytesseract
import numpy
# Create your views here.
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
FaviconView = RedirectView.as_view(url='/static/favicon.ico', permanent=True)

class IndexView(TemplateView):
    template_name = "index.html"
    
    def post(self,request):
        prediction = []
        confidence = []
        files = request.FILES.getlist("file")
        for i in UploadedFile.objects.filter(user=request.user.id):
            try:
                os.remove("./home/media/"+str(i.id))
            except:
                pass
        
        a = UploadedFile.objects.filter(user__id=request.user.id)
        a.delete()
        for image in files:
            p,c = assessment(image)
            newfile = UploadedFile(file=image)
            newfile.save()
            with open("./home/media/"+str(newfile.id), 'wb') as f:
                for chunk in image.chunks():
                    f.write(chunk)
            if p == "Good":
                img = cv2.imread("./home/media/"+str(newfile.id), cv2.COLOR_BGR2GRAY)
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                text = pytesseract.image_to_string(gray)
                newfile.quality = p
                newfile.ocr = text
                newfile.save()
            elif p == "Moderate":
                text = None
            else:
                text = None
            newfile = UploadedFile(file=image,quality=p,ocr=text)
            newfile.save()
            request.user.files.add(newfile)
            prediction.append(p)
            confidence.append(c)            
        out = zip(prediction,confidence,files,UploadedFile.objects.filter(user__email=request.user.email))
        good = (prediction.count("Good")*100)/len(files)
        moderate = (prediction.count("Moderate")*100)/len(files)
        poor = (prediction.count("Poor")*100)/len(files)
        return render(request,"dashboard.html",{"Output":out,"good":good,"moderate":moderate,"poor":poor,"totalfiles":len(files)})

class LogoutView(RedirectView):
    permanent = True
    pattern_name = 'login'

    def get_redirect_url(self, *args, **kwargs):
        logout(self.request)
        return super().get_redirect_url(*args, **kwargs)


class LoginView(TemplateView):
    template_name = "authentication/login.html"

    def post(self, request, *args, **kwargs):
            form1 = UserLoginForm(data=request.POST)
            form2 = UserCreationForm(request.POST)
            if form1.is_valid():
                user = authenticate(request,email=request.POST.get("username",""),password=request.POST.get("password",""))
                login(request,user)
                return redirect("/dashboard")
            elif form2.is_valid():
                user = form.save()
                login(request,user)
                return redirect("/dashboard")
            else:
                return self.render_to_response({"form1":form1,"form2":form2})

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("/dashboard/")
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form1"] = UserLoginForm()
        context["form2"] = UserCreationForm()
        return context


@csrf_exempt
def ChatView(request):
    msg = json.loads(request.body).get("message","")
    out = MessageChatBot(msg)
    return JsonResponse(data={"message":out})
        

class PasswordChangeView(TemplateView):
    template_name = "authentication/passwordchange.html"

    def post(self, request, *args, **kwargs):
        form = PasswordChangeForm(request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request,user)
            return render(request,"authentication/passworddone.html")
        else:
            return self.render_to_response({"form":form})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = PasswordChangeForm(self.request.user)
        return context

class DashboardView(LoginRequiredMixin,TemplateView):
    template_name = "dashboard.html"

    login_url = '/login'
    redirect_field_name = 'redirect_to'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

