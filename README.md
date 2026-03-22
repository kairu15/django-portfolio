# Portfolio Website

A comprehensive Django portfolio website inspired by Marco Polo Plaza Cebu's elegant design aesthetic. This project showcases professional web development skills with a focus on clean code, responsive design, and modern web technologies.

## Features

### Core Sections
- **Home Page**: Hero section with profile photo, navigation menu, and featured projects
- **About**: Personal background, career goals, and social media links
- **Skills**: Technical, professional, and soft skills with proficiency levels
- **Projects**: Portfolio showcase with project details, technologies used, and GitHub links
- **Education**: Academic background and qualifications
- **Contact**: Contact form with email functionality and social media integration

### Django Features Demonstrated
- ✅ Django project and app structure
- ✅ URL routing and views
- ✅ Models and database integration
- ✅ Django admin panel for content management
- ✅ Templates with template inheritance
- ✅ Forms handling and validation
- ✅ Static files management (CSS, JavaScript, images)
- ✅ Media files handling (uploads)
- ✅ Email functionality for contact form

### Design Features
- **Marco Polo Plaza Inspired Design**: Elegant color scheme with deep blues and gold accents
- **Responsive Design**: Mobile-first approach using Bootstrap 5
- **Modern UI**: Clean, professional interface with smooth animations
- **Accessibility**: Semantic HTML5 and ARIA-friendly structure
- **Interactive Elements**: Hover effects, smooth scrolling, and dynamic content

## Technology Stack

### Backend
- **Django 4.2.7**: Web framework
- **SQLite**: Database (development)
- **Pillow**: Image processing for profile photos and project images

### Frontend
- **HTML5**: Semantic markup
- **CSS3**: Custom styling with CSS variables
- **Bootstrap 5**: Responsive framework
- **Font Awesome 6**: Icons
- **JavaScript**: Interactive features and animations

### Development Tools
- **Python**: Programming language
- **Git**: Version control

## Project Structure

```
portfolio/
├── manage.py                 # Django management script
├── requirements.txt          # Python dependencies
├── portfolio/               # Django project directory
│   ├── __init__.py
│   ├── asgi.py             # ASGI configuration
│   ├── settings.py         # Django settings
│   ├── urls.py            # Main URL configuration
│   └── wsgi.py            # WSGI configuration
├── core/                   # Main Django app
│   ├── __init__.py
│   ├── admin.py           # Django admin configuration
│   ├── apps.py           # App configuration
│   ├── forms.py          # Form classes
│   ├── models.py         # Database models
│   ├── urls.py           # App URL configuration
│   ├── views.py          # View functions
│   └── templatetags/     # Custom template filters
│       ├── __init__.py
│       └── skill_filters.py
├── templates/             # HTML templates
│   ├── base.html         # Base template
│   └── core/            # App-specific templates
│       ├── home.html
│       ├── about.html
│       ├── skills.html
│       ├── projects.html
│       ├── education.html
│       ├── contact.html
│       └── contact_success.html
├── static/               # Static files
│   ├── css/
│   │   └── style.css    # Custom styles
│   ├── js/
│   │   └── script.js    # Custom JavaScript
│   └── images/          # Static images
└── media/               # User-uploaded files
    ├── profile/         # Profile photos
    └── projects/        # Project images
```

## Installation

### Prerequisites
- Python 3.8+
- pip (Python package manager)

### Setup Instructions

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd portfolio
   ```

2. **Create and activate virtual environment**
   ```bash
   python -m venv venv
   
   # Windows
   venv\Scripts\activate
   
   # macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**
   - Update `portfolio/settings.py` with your configuration
   - Set `SECRET_KEY` to a secure value
   - Update `DEFAULT_FROM_EMAIL` for contact form functionality
   - Configure database settings if needed

5. **Run database migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Create superuser for admin access**
   ```bash
   python manage.py createsuperuser
   ```

7. **Collect static files**
   ```bash
   python manage.py collectstatic
   ```

8. **Run the development server**
   ```bash
   python manage.py runserver
   ```

9. **Access the application**
   - Website: http://127.0.0.1:8000/
   - Admin Panel: http://127.0.0.1:8000/admin/

## Usage

### Admin Panel Configuration

1. **Access Admin Panel**
   - Navigate to `/admin/`
   - Login with superuser credentials

2. **Add Portfolio Content**
   - **About**: Add your personal information, tagline, and social media links
   - **Skills**: Add technical, professional, and soft skills with proficiency levels
   - **Projects**: Add portfolio projects with descriptions and technologies
   - **Education**: Add your educational background

3. **Manage Contact Messages**
   - View and manage messages submitted through the contact form
   - Messages are stored in the database and optionally sent via email

### Customization

#### Colors and Theme
The design uses CSS variables defined in `static/css/style.css`:
```css
:root {
    --primary-color: #1a3a52;    /* Deep blue */
    --secondary-color: #d4af37;  /* Gold accent */
    --accent-color: #2c5f7c;     /* Lighter blue */
    /* ... more variables */
}
```

#### Adding New Sections
1. Create models in `core/models.py`
2. Add views in `core/views.py`
3. Create templates in `templates/core/`
4. Update URL configuration in `core/urls.py`

#### Email Configuration
For production email functionality:
1. Update `EMAIL_BACKEND` in `settings.py`
2. Configure SMTP settings
3. Set `DEFAULT_FROM_EMAIL`

## Deployment

### Production Considerations

1. **Security**
   - Set `DEBUG = False`
   - Configure `ALLOWED_HOSTS`
   - Use environment variables for sensitive data
   - Set up HTTPS

2. **Database**
   - Consider PostgreSQL for production
   - Configure database connection settings

3. **Static Files**
   - Configure static file serving
   - Use CDN for better performance

4. **Email**
   - Configure production email backend
   - Set up email templates

### Example Deployment Platforms
- **Heroku**: Easy deployment with PostgreSQL
- **DigitalOcean**: Full control over server
- **AWS**: Scalable cloud infrastructure
- **PythonAnywhere**: Simple Python hosting

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is open source and available under the [MIT License](LICENSE).

## Support

For questions or support:
- Create an issue in the repository
- Contact through the portfolio website's contact form

## Acknowledgments

- Design inspiration from Marco Polo Plaza Cebu
- Built with Django and Bootstrap 5
- Icons by Font Awesome
- Thanks to the open-source community

---

**Note**: This is a portfolio project demonstrating web development skills. Feel free to customize and adapt it for your own use case.
