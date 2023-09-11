from django.contrib import admin
from django.urls import path
from myApp.views import InfoView

urlpatterns = [
    path("", get_data.view, name=""),
    
    path("admin/", admin.site.urls),
]
