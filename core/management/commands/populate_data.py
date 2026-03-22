from django.core.management.base import BaseCommand
from django.utils import timezone
from core.models import About, Skill, Project, Education


class Command(BaseCommand):
    help = 'Populate the database with sample portfolio data'

    def handle(self, *args, **options):
        self.stdout.write('Creating sample portfolio data...')

        # Create About entry
        about, created = About.objects.get_or_create(
            id=1,
            defaults={
                'name': 'John Doe',
                'tagline': 'Full Stack Developer | Creative Problem Solver',
                'personal_background': 'I am a passionate full-stack developer with 5+ years of experience in creating innovative digital solutions. My journey in technology began with a curiosity about how things work on the internet, and it has evolved into a career focused on creating meaningful digital experiences that make a difference.',
                'career_goals': 'My goal is to continue growing as a developer while working on challenging projects that push the boundaries of what\'s possible. I aspire to lead development teams, mentor junior developers, and contribute to open-source projects that benefit the community.',
                'email': 'john.doe@example.com',
                'linkedin': 'https://linkedin.com/in/johndoe',
                'github': 'https://github.com/johndoe',
                'twitter': 'https://twitter.com/johndoe'
            }
        )
        if created:
            self.stdout.write(self.style.SUCCESS('Created About entry'))
        else:
            self.stdout.write(self.style.WARNING('About entry already exists'))

        # Create Technical Skills
        technical_skills = [
            ('Python', 'technical', 4),
            ('Django', 'technical', 4),
            ('JavaScript', 'technical', 4),
            ('React', 'technical', 3),
            ('HTML5/CSS3', 'technical', 4),
            ('PostgreSQL', 'technical', 3),
            ('Git', 'technical', 4),
            ('Docker', 'technical', 2),
            ('AWS', 'technical', 2),
            ('REST API Design', 'technical', 4)
        ]

        for name, category, proficiency in technical_skills:
            skill, created = Skill.objects.get_or_create(
                name=name,
                defaults={
                    'category': category,
                    'proficiency_level': proficiency
                }
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Created technical skill: {name}'))

        # Create Professional Skills
        professional_skills = [
            ('Project Management', 'professional', 3),
            ('Team Leadership', 'professional', 3),
            ('Agile/Scrum', 'professional', 4),
            ('Client Communication', 'professional', 4),
            ('Problem Solving', 'professional', 4),
            ('Time Management', 'professional', 3),
            ('Documentation', 'professional', 3),
            ('Code Review', 'professional', 3)
        ]

        for name, category, proficiency in professional_skills:
            skill, created = Skill.objects.get_or_create(
                name=name,
                defaults={
                    'category': category,
                    'proficiency_level': proficiency
                }
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Created professional skill: {name}'))

        # Create Soft Skills
        soft_skills = [
            ('Communication', 'soft', 4),
            ('Creativity', 'soft', 4),
            ('Adaptability', 'soft', 4),
            ('Critical Thinking', 'soft', 3),
            ('Collaboration', 'soft', 4),
            ('Mentoring', 'soft', 3),
            ('Public Speaking', 'soft', 2)
        ]

        for name, category, proficiency in soft_skills:
            skill, created = Skill.objects.get_or_create(
                name=name,
                defaults={
                    'category': category,
                    'proficiency_level': proficiency
                }
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Created soft skill: {name}'))

        # Create Projects
        projects_data = [
            {
                'title': 'E-Commerce Platform',
                'description': 'A full-featured e-commerce platform built with Django and React. Includes user authentication, product catalog, shopping cart, payment integration, and admin dashboard.',
                'technologies': 'Django, React, PostgreSQL, Stripe API, Docker',
                'github_link': 'https://github.com/johndoe/ecommerce-platform',
                'live_demo': 'https://ecommerce-demo.example.com',
                'featured': True,
                'completion_date': timezone.now().date()
            },
            {
                'title': 'Task Management System',
                'description': 'A collaborative task management application with real-time updates, drag-and-drop functionality, team collaboration features, and comprehensive reporting.',
                'technologies': 'Django, JavaScript, Bootstrap, WebSocket, PostgreSQL',
                'github_link': 'https://github.com/johndoe/task-manager',
                'live_demo': 'https://taskmanager-demo.example.com',
                'featured': True,
                'completion_date': timezone.now().date()
            },
            {
                'title': 'Weather Dashboard',
                'description': 'A responsive weather dashboard that provides real-time weather information, forecasts, and interactive maps. Features location-based weather updates and historical data visualization.',
                'technologies': 'Django, JavaScript, Chart.js, OpenWeather API, REST API',
                'github_link': 'https://github.com/johndoe/weather-dashboard',
                'live_demo': 'https://weather-demo.example.com',
                'featured': True,
                'completion_date': timezone.now().date()
            },
            {
                'title': 'Blog Platform',
                'description': 'A modern blogging platform with markdown support, user authentication, comment system, and SEO optimization. Includes admin panel for content management.',
                'technologies': 'Django, PostgreSQL, Markdown, Bootstrap, SEO',
                'github_link': 'https://github.com/johndoe/blog-platform',
                'featured': False,
                'completion_date': timezone.now().date()
            },
            {
                'title': 'API Gateway Service',
                'description': 'A microservices API gateway that handles authentication, rate limiting, request routing, and response aggregation for multiple backend services.',
                'technologies': 'Django, Django REST Framework, Redis, Docker, Kubernetes',
                'github_link': 'https://github.com/johndoe/api-gateway',
                'featured': False,
                'completion_date': timezone.now().date()
            }
        ]

        for project_data in projects_data:
            project, created = Project.objects.get_or_create(
                title=project_data['title'],
                defaults=project_data
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Created project: {project.title}'))

        # Create Education entries
        education_data = [
            {
                'school': 'University of Technology',
                'degree': 'Bachelor of Science in Computer Science',
                'start_year': 2016,
                'end_year': 2020,
                'description': 'Graduated with honors. Focus on software engineering, algorithms, and database systems. Active member of the coding club and participated in hackathons.'
            },
            {
                'school': 'Tech Institute',
                'degree': 'Full Stack Web Development Bootcamp',
                'start_year': 2020,
                'end_year': 2020,
                'description': 'Intensive 6-month program covering modern web development technologies including React, Node.js, and cloud deployment.'
            }
        ]

        for edu_data in education_data:
            education, created = Education.objects.get_or_create(
                school=edu_data['school'],
                degree=edu_data['degree'],
                defaults=edu_data
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Created education entry: {education.school}'))

        self.stdout.write(self.style.SUCCESS('Sample data creation completed!'))
