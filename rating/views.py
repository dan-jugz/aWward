from django.shortcuts import render
from .models  import Project

# Create your views here.
def index(request):
 
    projects = Project.objects.order_by('-overall').all()
    runners=Project.objects.all()[:4]
    
    return render(request, 'index.html', locals())
