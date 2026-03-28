from django.core.management.base import BaseCommand
from django.core.files import File
from core.models import Project
import os
from pathlib import Path

class Command(BaseCommand):
    help = 'Assign existing images to projects based on project titles'

    def handle(self, *args, **options):
        # Define image mappings based on available images
        image_mappings = {
            'Hotel Management System': 'hotel-management/HotelManagementSystem.png',
            'Learning Management System': 'lms/LMS.png',
            'Voting System': 'voting-system/VotingSystem.png',
        }
        
        static_root = Path('static/images')
        
        for project_title, image_path in image_mappings.items():
            # Find project by title
            try:
                project = Project.objects.get(title__icontains=project_title)
                
                # Get the full image path
                full_image_path = static_root / image_path
                
                if full_image_path.exists():
                    # Open the image file and assign it to the project
                    with open(full_image_path, 'rb') as f:
                        project.featured_image.save(
                            os.path.basename(image_path),
                            File(f),
                            save=True
                        )
                    self.stdout.write(
                        self.style.SUCCESS(f'Assigned {image_path} to project "{project.title}"')
                    )
                else:
                    self.stdout.write(
                        self.style.WARNING(f'Image file {full_image_path} not found')
                    )
                    
            except Project.DoesNotExist:
                # Create the project if it doesn't exist
                project_data = self.get_project_data(project_title)
                if project_data:
                    project = Project.objects.create(**project_data)
                    
                    # Assign the image
                    full_image_path = static_root / image_path
                    if full_image_path.exists():
                        with open(full_image_path, 'rb') as f:
                            project.featured_image.save(
                                os.path.basename(image_path),
                                File(f),
                                save=True
                            )
                        self.stdout.write(
                            self.style.SUCCESS(f'Created project "{project.title}" and assigned image')
                        )
                    else:
                        self.stdout.write(
                            self.style.WARNING(f'Image file {full_image_path} not found for new project')
                        )
                else:
                    self.stdout.write(
                        self.style.WARNING(f'No data available for project "{project_title}"')
                    )
        
        self.stdout.write(self.style.SUCCESS('Image assignment completed!'))

    def get_project_data(self, project_title):
        """Return project data for creating new projects"""
        project_data = {
            'Hotel Management System': {
                'title': 'Hotel Management System',
                'description': 'A comprehensive hotel management system with booking, room management, and customer service features.',
                'technologies': 'Python, Django, PostgreSQL, HTML, CSS, JavaScript, Bootstrap',
                'github_link': 'https://github.com/example/hotel-management',
                'live_demo': 'https://hotel-demo.example.com',
                'featured': True,
                'completion_date': '2024-01-15'
            },
            'Learning Management System': {
                'title': 'Learning Management System',
                'description': 'A web-based Learning Management System built using PHP. It includes features such as user registration, login, course management, and content delivery. This project showcases my skills in backend development and database integration.',
                'technologies': 'PHP, MySQL, HTML, CSS, JavaScript, Bootstrap',
                'github_link': 'https://github.com/example/lms',
                'live_demo': 'https://lms-demo.example.com',
                'featured': True,
                'completion_date': '2025-03-10'
            },
            'Voting System': {
                'title': 'Voting System',
                'description': 'A console-based voting system developed using C++. It allows users to cast votes, count results, and display winners efficiently. This project demonstrates basic programming logic, data handling, and user interaction in C++.',
                'technologies': 'C++, Console Application, Data Structures, Algorithms',
                'github_link': 'https://github.com/example/voting-system',
                'live_demo': 'https://voting-demo.example.com',
                'featured': True,
                'completion_date': '2024-03-10'
            }
        }
        
        return project_data.get(project_title)
