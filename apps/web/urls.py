from django.urls import path
from apps.web import views

urlpatterns = [
    path('auth/',views.auth,name="auth"),
]
