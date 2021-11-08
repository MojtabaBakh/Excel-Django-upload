from django.urls import path , include

from . import views

app_name = "myapp"

urlpatterns = [
    path('upload/',views.savedata , name='save'),
    path('list/',views.showdata , name='list'),
    path('',views.home , name='home'),
    

]
