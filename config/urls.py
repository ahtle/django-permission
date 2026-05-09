"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
"""
from django.contrib import admin
from django.http import JsonResponse
from django.urls import include, path

def healthcheck(request):
    return JsonResponse({
        "status": "ok",
    })

urlpatterns = [
    path('', healthcheck),
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
]
