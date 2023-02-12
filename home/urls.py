from django.urls import path
from .views import IndexView,FaviconView,LoginView,PasswordChangeView,DashboardView,LogoutView,ChatView
urlpatterns = [
    path("",IndexView.as_view(),name="new"), # Landing page that user will see.
    path("login/",LoginView.as_view(),name="login"), # User can login here.
    path("logout/",LogoutView.as_view(),name="logout"), # User can login here.
    path("change_password/",PasswordChangeView.as_view(),name="change_password"), # User can change their password here.
    path("dashboard/",DashboardView.as_view(),name="dashboard"), # Main Dashboard here.
    path("chat/",ChatView,name="chat"), # Chat API
    path('favicon.ico', FaviconView), # For favicon
]