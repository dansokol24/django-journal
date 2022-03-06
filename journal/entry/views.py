from django.shortcuts import render

from .models import Entry

# Create your views here.
def index(request):
    query = Entry.objects.all()