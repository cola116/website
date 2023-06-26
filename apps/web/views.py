from django.shortcuts import render

# Create your views here.


from django.shortcuts import render, HttpResponse


def auth(request):
    return HttpResponse("auth_web")
