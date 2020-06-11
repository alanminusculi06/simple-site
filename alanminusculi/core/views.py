from django.shortcuts import render
from .models import Identity, Skill


def home(request):
    template_name = 'home.html'
    identity = Identity.objects.filter().first()
    ctx = {
        'identity': identity
    }
    return render(request, template_name, ctx)


def skills(request):
    template_name = 'habilidades.html'    
    skills = Skill.objects.filter()
    ctx = {
        'skills': skills
    }
    return render(request, template_name, ctx)
