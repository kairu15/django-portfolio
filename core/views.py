from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings
from .models import About, Skill, Project, Education, ContactMessage


def home(request):
    about = About.objects.first()
    featured_projects = Project.objects.filter(featured=True)[:3]
    context = {
        'about': about,
        'featured_projects': featured_projects,
    }
    return render(request, 'core/home.html', context)


def about(request):
    about = About.objects.first()
    context = {
        'about': about,
    }
    return render(request, 'core/about.html', context)


def skills(request):
    technical_skills = Skill.objects.filter(category='technical').order_by('name')
    professional_skills = Skill.objects.filter(category='professional').order_by('name')
    soft_skills = Skill.objects.filter(category='soft').order_by('name')
    
    context = {
        'technical_skills': technical_skills,
        'professional_skills': professional_skills,
        'soft_skills': soft_skills,
    }
    return render(request, 'core/skills.html', context)


def projects(request):
    projects = Project.objects.all().order_by('-completion_date', '-featured')
    context = {
        'projects': projects,
    }
    return render(request, 'core/projects.html', context)


def education(request):
    education_list = Education.objects.all().order_by('-start_year')
    context = {
        'education_list': education_list,
    }
    return render(request, 'core/education.html', context)


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        ContactMessage.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message
        )
        
        try:
            send_mail(
                f'Portfolio Contact: {subject}',
                f'From: {name} ({email})\n\n{message}',
                settings.DEFAULT_FROM_EMAIL,
                [settings.DEFAULT_FROM_EMAIL],
                fail_silently=False,
            )
            messages.success(request, 'Your message has been sent successfully!')
        except:
            messages.success(request, 'Your message has been saved. We will get back to you soon!')
        
        return redirect('contact_success')
    
    about = About.objects.first()
    context = {
        'about': about,
    }
    return render(request, 'core/contact.html', context)


def contact_success(request):
    return render(request, 'core/contact_success.html')
