from django.shortcuts import render,redirect
from django.http import HttpResponse, Http404
from django.contrib.auth.decorators import login_required
from .models  import Project,Profile,Rating,categories,technologies
from .forms import ProfileForm, UploadForm, RatingForm
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
@login_required(login_url='/accounts/login')
def index(request):
    current_user = request.user 
    projects = Project.objects.order_by('-overall').all()
    runners=Project.objects.all()[:4]
    
    return render(request, 'index.html', locals())


@login_required(login_url='/accounts/login')
def profile(request):
    
    return render(request, 'profile.html', locals())


@login_required(login_url='/accounts/login')
def edit_profile(request):

    return render(request, 'edit_profile.html', locals())

@login_required(login_url='/accounts/login')
def new_project(request):

    return render(request, 'new_project.html', locals())

@login_required(login_url='/accounts/login')
def project(request):

    return render(request, 'project.html', locals())