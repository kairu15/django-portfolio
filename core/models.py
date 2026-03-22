from django.db import models
from django.urls import reverse


class About(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField()
    profile_photo = models.ImageField(upload_to='profile/', blank=True, null=True)
    personal_background = models.TextField()
    career_goals = models.TextField()
    email = models.EmailField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    github = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)
    
    class Meta:
        verbose_name_plural = "About"
    
    def __str__(self):
        return self.name


class Skill(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50, choices=[
        ('technical', 'Technical'),
        ('professional', 'Professional'),
        ('soft', 'Soft Skills'),
    ])
    proficiency_level = models.IntegerField(choices=[
        (1, 'Beginner'),
        (2, 'Intermediate'),
        (3, 'Advanced'),
        (4, 'Expert'),
    ])
    
    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    technologies = models.TextField(help_text="Comma-separated list of technologies")
    github_link = models.URLField(blank=True, null=True)
    live_demo = models.URLField(blank=True, null=True)
    featured_image = models.ImageField(upload_to='projects/', blank=True, null=True)
    completion_date = models.DateField(blank=True, null=True)
    featured = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title
    
    def get_technologies_list(self):
        return [tech.strip() for tech in self.technologies.split(',')]


class Education(models.Model):
    school = models.CharField(max_length=200)
    degree = models.CharField(max_length=200)
    start_year = models.IntegerField()
    end_year = models.IntegerField()
    description = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return f"{self.degree} - {self.school}"


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.name} - {self.subject}"
