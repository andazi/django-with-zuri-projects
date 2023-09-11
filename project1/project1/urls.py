from django.contrib import admin
from django.urls import path
from myApp.views import get_data

urlpatterns = [
    path("", get_data, name="track"),
    
    path("admin/", admin.site.urls),
]
