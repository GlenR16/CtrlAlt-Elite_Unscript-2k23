from django.urls import path
from .views import IndexView,FaviconView,LoginView,SignupView,PasswordChangeView,DashboardView,FeedbackView,LogoutView,ProfileView,ChatView, demo
urlpatterns = [
    path("",IndexView.as_view(),name="index"), # Landing page that user will see.
    path("login/",LoginView.as_view(),name="login"), # User can login here.
    path("logout/",LogoutView.as_view(),name="logout"), # User can login here.
    path("signup/",SignupView.as_view(),name="signup"), # User can signup here.
    path("change_password/",PasswordChangeView.as_view(),name="change_password"), # User can change their password here.
    path("dashboard/",DashboardView.as_view(),name="dashboard"), # Main Dashboard here.
    path("chat/",ChatView,name="chat"), # Main Dashboard here.
    path("feedback/",FeedbackView.as_view(),name="feedback"), # Feedback Page
    path("profile/",ProfileView.as_view(),name="profile"), # Profile Page
    path('favicon.ico', FaviconView), # For favicon
    path('demo/', demo, name='demo'),
]