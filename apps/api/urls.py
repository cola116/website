from django.urls import path
from apps.api import views

urlpatterns = [
    path('auth/',views.auth,name="auth"),
    path('login/',views.login,name="login")
]
