from django.db import models


class HeroSection(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=300)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='hero/', blank=True, null=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Hero Section'
        verbose_name_plural = 'Hero Sections'

    def __str__(self):
        return self.title


class UniversityStats(models.Model):
    total_students = models.PositiveIntegerField(default=5000)
    total_faculty = models.PositiveIntegerField(default=300)
    total_courses = models.PositiveIntegerField(default=200)
    success_rate = models.PositiveIntegerField(default=99, help_text='Percentage')
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'University Statistics'
        verbose_name_plural = 'University Statistics'

    def __str__(self):
        return f'Stats ({self.total_students} students)'


class Feature(models.Model):
    WHY_CHOOSE = 'why_choose'
    LMS_FEATURES = 'lms_features'
    SECTION_CHOICES = [
        (WHY_CHOOSE, 'Why Choose KIU LMS'),
        (LMS_FEATURES, 'LMS Features'),
    ]

    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    icon = models.CharField(max_length=50, blank=True)
    section = models.CharField(max_length=20, choices=SECTION_CHOICES, default=LMS_FEATURES)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['section', 'order']

    def __str__(self):
        return self.title


class Announcement(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title


class ContactInfo(models.Model):
    email = models.EmailField()
    phone = models.CharField(max_length=30)
    address = models.TextField()
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Contact Information'
        verbose_name_plural = 'Contact Information'

    def __str__(self):
        return self.email


class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100, blank=True)
    content = models.TextField()
    rating = models.PositiveSmallIntegerField(default=5)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.name


class FAQ(models.Model):
    question = models.CharField(max_length=300)
    answer = models.TextField()
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['order']
        verbose_name = 'FAQ'
        verbose_name_plural = 'FAQs'

    def __str__(self):
        return self.question
