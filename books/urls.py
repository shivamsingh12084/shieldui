from tkinter import N
from django.urls import include , path
from rest_framework import routers
from . import views
from .views import HomePageView
 
router = routers.DefaultRouter()
router.register(r'catalog', views.BookViewSet)
 
urlpatterns = [
    path('api/', include(router.urls)),
    path('home/', HomePageView.as_view(), name='home'),
]