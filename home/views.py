from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic

# Create your views here.
def index(request):
    return render(request, 'home/index.html')

class AboutView(generic.View):
    
    def get(self, request, *args, **kwargs):
        return render(request, 'home/about.html')