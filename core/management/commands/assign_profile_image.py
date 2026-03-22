from django.core.management.base import BaseCommand
from django.core.files import File
from core.models import About
import os
from pathlib import Path

class Command(BaseCommand):
    help = 'Assign profile image to About model'

    def handle(self, *args, **options):
        # Path to the profile image
        profile_image_path = Path('static/images/profile/Profile.jpg')
        
        # Get or create the About instance
        about = About.objects.first()
        if not about:
            # Create a default About instance if none exists
            about = About.objects.create(
                name="Your Name",
                tagline="Full Stack Developer | Creative Problem Solver",
                personal_background="Welcome to my portfolio! I'm a passionate developer with expertise in creating innovative digital solutions.",
                career_goals="To become a senior software engineer and lead development teams in building impactful applications.",
                email="your.email@example.com",
                linkedin="https://linkedin.com/in/yourprofile",
                github="https://github.com/yourusername",
                twitter="https://twitter.com/yourusername"
            )
            self.stdout.write(
                self.style.SUCCESS('Created default About instance')
            )
        
        # Assign the profile image if it exists
        if profile_image_path.exists():
            with open(profile_image_path, 'rb') as f:
                about.profile_photo.save(
                    'Profile.jpg',
                    File(f),
                    save=True
                )
            self.stdout.write(
                self.style.SUCCESS(f'Assigned profile image to About instance')
            )
        else:
            self.stdout.write(
                self.style.WARNING(f'Profile image {profile_image_path} not found')
            )
        
        self.stdout.write(self.style.SUCCESS('Profile image assignment completed!'))
