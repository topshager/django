from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.main, name='main'),
    path('admin/', admin.site.urls),
    path('tennis_app/', views.members, name='tennis_app'),
    path('tennis_app/details/<int:id>',views.details,name='details'),
    path('testing/',views.testing, name='testing'),

]
