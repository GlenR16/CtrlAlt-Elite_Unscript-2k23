from django.shortcuts import render,redirect
from django.views.generic.base import TemplateView,RedirectView,View
from .forms import UserCreationForm,UserLoginForm,PasswordChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login,logout,authenticate,update_session_auth_hash
from django.http import JsonResponse
from .chatbot.chatbot import message as MessageChatBot
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.
FaviconView = RedirectView.as_view(url='/static/favicon.ico', permanent=True)

class IndexView(TemplateView):
    template_name = "index.html"

class LogoutView(RedirectView):
    permanent = True
    pattern_name = 'login'

    def get_redirect_url(self, *args, **kwargs):
        logout(self.request)
        return super().get_redirect_url(*args, **kwargs)


class LoginView(TemplateView):
    template_name = "authentication/login.html"

    def post(self, request, *args, **kwargs):
            form = UserLoginForm(data=request.POST)
            if form.is_valid():
                user = authenticate(request,email=request.POST.get("username",""),password=request.POST.get("password",""))
                login(request,user)
                return redirect("/dashboard")
            else:
                return self.render_to_response({"form":form})

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("/dashboard/")
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = UserLoginForm()
        return context

class SignupView(TemplateView):
    template_name = "authentication/signup.html"

    def post(self, request, *args, **kwargs):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect("/dashboard")
        else:
            return self.render_to_response({"form":form})

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("/dashboard/")
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = UserCreationForm()
        return context

class ProfileView(LoginRequiredMixin,TemplateView):
    template_name = "profile.html"

    login_url = '/login'
    redirect_field_name = 'redirect_to'

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)

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

class FeedbackView(TemplateView,LoginRequiredMixin):
    template_name = "feedback.html"