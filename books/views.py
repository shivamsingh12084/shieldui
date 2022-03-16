from django.shortcuts import render
from rest_framework import viewsets
from .serializers import BookSerializer
from .models import Book
from django.views.generic import TemplateView
 
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all().order_by('-id')
    serializer_class = BookSerializer

class HomePageView(TemplateView):
    template_name = 'home.html'