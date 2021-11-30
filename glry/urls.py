from django.contrib import admin
from . import views
from django.urls import path
from django.conf.urls.static import static


# from photos import views 

app_name = 'glry'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('location/', views.image_location, name='food'),

]
