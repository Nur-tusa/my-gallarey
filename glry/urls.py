from django.contrib import admin
from . import views
from django.urls import path
# from photos import views
app_name = 'glry'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
]