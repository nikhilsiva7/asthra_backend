
from django.urls import path
from .views import RegisterAlumniView, LoginView, LogoutView

urlpatterns = [
    path('register/alumni/', RegisterAlumniView.as_view(), name='register_alumni'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]