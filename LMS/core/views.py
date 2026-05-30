from django.shortcuts import render

from .models import (
    Announcement,
    ContactInfo,
    FAQ,
    Feature,
    HeroSection,
    Testimonial,
    UniversityStats,
)

FEATURED_COURSES = [
    {
        'title': 'Introduction to Programming',
        'description': 'Learn programming fundamentals with Python and problem-solving techniques.',
        'icon': '💻',
    },
    {
        'title': 'Web Development',
        'description': 'Build modern responsive websites using HTML, CSS, and JavaScript.',
        'icon': '🌐',
    },
    {
        'title': 'Database Systems',
        'description': 'Design, query, and manage relational databases for real-world applications.',
        'icon': '🗄️',
    },
    {
        'title': 'Artificial Intelligence',
        'description': 'Explore machine learning, neural networks, and intelligent systems.',
        'icon': '🤖',
    },
    {
        'title': 'Data Structures',
        'description': 'Master algorithms and data structures for efficient software development.',
        'icon': '📊',
    },
]

def _get_hero():
    return HeroSection.objects.filter(is_active=True).first()


def _get_stats():
    stats = UniversityStats.objects.filter(is_active=True).first()
    if stats:
        return stats
    return UniversityStats(
        total_students=5000,
        total_faculty=300,
        total_courses=200,
        success_rate=99,
    )


def _get_contact():
    return ContactInfo.objects.filter(is_active=True).first()


def homepage(request):
    context = {
        'hero': _get_hero(),
        'stats': _get_stats(),
        'why_choose': Feature.objects.filter(section=Feature.WHY_CHOOSE),
        'lms_features': Feature.objects.filter(section=Feature.LMS_FEATURES),
        'featured_courses': FEATURED_COURSES,
        'announcements': Announcement.objects.filter(is_published=True)[:5],
        'testimonials': Testimonial.objects.filter(is_active=True)[:6],
        'contact': _get_contact(),
    }
    return render(request, 'core/homepage.html', context)


def about(request):
    return render(request, 'core/about.html', {'stats': _get_stats()})


def contact(request):
    return render(request, 'core/contact.html', {'contact': _get_contact()})


def faq(request):
    return render(
        request,
        'core/faq.html',
        {'faqs': FAQ.objects.filter(is_active=True)},
    )


def login_view(request):
    return render(request, 'core/login.html')


def register_view(request):
    return render(request, 'core/register.html')


def dashboard(request):
    from django.utils import timezone

    context = {
        'student_name': 'Farhan',
        'current_date': timezone.now().strftime('%a, %b %d, %Y'),
        'current_courses': 5,
        'assignments_due': 3,
        'attendance': 92,
        'cgpa': 3.6,
        'live_classes': [
            {
                'status': 'active',
                'code': 'CS301: Advanced Data Structures',
                'instructor': 'Dr. Alice Smith',
                'time': '',
            },
            {
                'status': 'upcoming',
                'code': 'MA102: Linear Algebra',
                'instructor': '',
                'time': '10:30 AM',
            },
            {
                'status': 'upcoming',
                'code': 'PHY201: Waves and Optics',
                'instructor': '',
                'time': '1:15 PM',
            },
        ],
        'assignment_deadlines': [
            {'date': 'Oct. 26 12:00 AM', 'name': 'Tasks', 'progress': 52, 'color': 'blue'},
            {'date': 'Oct. 28', 'name': 'Draiffactor', 'progress': 25, 'color': 'navy'},
            {'date': 'Oct. 28', 'name': 'Task Evaneats', 'progress': 31, 'color': 'gold'},
        ],
        'quick_access': [
            {'title': 'Generate Fee Challan', 'icon': '💳', 'color': 'blue', 'url': '#'},
            {'title': 'Transport', 'icon': '🚚', 'color': 'orange', 'url': '#'},
            {'title': 'Admit Card', 'icon': '🪪', 'color': 'green', 'url': '#'},
            {'title': 'Noticeboard', 'icon': '📋', 'color': 'pink', 'url': '#'},
            {'title': 'Arrange Classes', 'icon': '⏱️', 'color': 'purple', 'url': '#'},
            {'title': 'Live Classes', 'icon': '📹', 'color': 'sky', 'url': '#'},
        ],
    }
    return render(request, 'core/dashboard/home.html', context)
