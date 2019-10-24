from django.shortcuts import render
from .models  import Project,Profile

# Create your views here.
def index(request):
 
    projects = Project.objects.order_by('-overall').all()
    runners=Project.objects.all()[:4]
    
    return render(request, 'index.html', locals())


def profile(request):

    return render(request, 'profile.html', locals())


def edit_profile(request):

    return render(request, 'edit_profile.html', locals())


def new_project(request):

    return render(request, 'new_project.html', locals())


def project(request):

    return render(request, 'project.html', locals())