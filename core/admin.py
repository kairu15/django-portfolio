from django.contrib import admin
from .models import About, Skill, Project, Education, ContactMessage


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'linkedin', 'github']
    search_fields = ['name']


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'proficiency_level']
    list_filter = ['category', 'proficiency_level']
    search_fields = ['name']


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'featured', 'completion_date', 'github_link']
    list_filter = ['featured', 'completion_date']
    search_fields = ['title', 'description']
    date_hierarchy = 'completion_date'


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ['school', 'degree', 'start_year', 'end_year']
    search_fields = ['school', 'degree']


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'created_at']
    list_filter = ['created_at']
    search_fields = ['name', 'email', 'subject']
    readonly_fields = ['created_at']
