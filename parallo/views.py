from django.shortcuts import render
from .models import themes
# Create your views here.
def index(request):
    theme1=themes()
    name:'Health'
    desc:'..coz health is wealth'
    
    theme2=themes()
    name:'Education'
    desc:'Explore the best education facilities nearby'
    
    theme3=themes()
    name:'Hygiene'
    desc:'Your hygeine is in your hands'
    
    theme=[theme1,theme2,theme3]
    
    return render(request, "index.html", {'theme':theme })