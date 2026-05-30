from django.db import migrations


def seed_homepage_data(apps, schema_editor):
    HeroSection = apps.get_model('core', 'HeroSection')
    UniversityStats = apps.get_model('core', 'UniversityStats')
    Feature = apps.get_model('core', 'Feature')
    Announcement = apps.get_model('core', 'Announcement')
    ContactInfo = apps.get_model('core', 'ContactInfo')
    Testimonial = apps.get_model('core', 'Testimonial')

    HeroSection.objects.get_or_create(
        title='Welcome to KIU Learning Management System',
        defaults={
            'subtitle': 'Learn Anytime, Anywhere',
            'description': 'Access courses, assignments, quizzes, announcements and academic resources from a single platform.',
            'is_active': True,
        },
    )

    UniversityStats.objects.get_or_create(
        is_active=True,
        defaults={'total_students': 5000, 'total_faculty': 300, 'total_courses': 200, 'success_rate': 99},
    )

    for order, title in enumerate([
        'Online Learning', 'Interactive Quizzes', 'Assignment Tracking',
        'Real Time Grades', 'Attendance Monitoring', 'Discussion Forums',
    ]):
        Feature.objects.get_or_create(title=title, section='why_choose', defaults={'order': order})

    for order, (title, desc, icon) in enumerate([
        ('Course Management', 'Manage all courses, materials, and schedules.', '📖'),
        ('Assignments', 'Submit assignments online and track deadlines.', '📝'),
        ('Quizzes', 'Take online examinations with instant feedback.', '✅'),
        ('Attendance', 'Track attendance for every class session.', '📅'),
        ('Messaging', 'Communicate instantly with instructors and peers.', '💬'),
        ('Analytics', 'Track academic progress with detailed insights.', '📈'),
    ]):
        Feature.objects.get_or_create(title=title, section='lms_features', defaults={'description': desc, 'icon': icon, 'order': order})

    for title, desc in [
        ('Mid Term Exams Starting from 10 June', 'Check your exam schedules on the portal.'),
        ('Holiday Notice', 'University will remain closed on public holidays.'),
        ('Course Registration Deadline', 'Last date to register is 20 June.'),
    ]:
        Announcement.objects.get_or_create(title=title, defaults={'description': desc})

    ContactInfo.objects.get_or_create(
        email='info@kiu.edu.pk',
        defaults={'phone': '+92 5815 961234', 'address': 'Karakoram International University, Gilgit, Pakistan', 'is_active': True},
    )

    for name, role, content in [
        ('Ayesha Khan', 'CS Student', 'This LMS made learning easier.'),
        ('Usman Ali', 'BA Student', 'Grade tracking keeps me on top of my progress.'),
        ('Dr. Sara Ahmed', 'Faculty', 'Managing courses has never been this efficient.'),
    ]:
        Testimonial.objects.get_or_create(name=name, defaults={'role': role, 'content': content, 'rating': 5})


class Migration(migrations.Migration):
    dependencies = [('core', '0001_initial')]
    operations = [migrations.RunPython(seed_homepage_data, migrations.RunPython.noop)]
