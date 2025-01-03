from django.urls import path
from . import views

urlpatterns = [
    path('tennis_app/', views.members, name='tennis_app'),
    path('tennis_app/details/<int:id>',views.details,name='details'),
]
