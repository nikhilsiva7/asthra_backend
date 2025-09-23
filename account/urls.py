from django.urls import path
from account.views import RegisterAlumniView, LoginView, LogoutView

urlpatterns = [
    path('register/alumni/', RegisterAlumniView.as_view(), name='register-alumni'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]