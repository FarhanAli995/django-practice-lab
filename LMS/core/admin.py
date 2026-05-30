from django.contrib import admin

from .models import (
    Announcement,
    ContactInfo,
    FAQ,
    Feature,
    HeroSection,
    Testimonial,
    UniversityStats,
)


@admin.register(HeroSection)
class HeroSectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active')
    list_filter = ('is_active',)


@admin.register(UniversityStats)
class UniversityStatsAdmin(admin.ModelAdmin):
    list_display = (
        'total_students',
        'total_faculty',
        'total_courses',
        'success_rate',
        'is_active',
    )


@admin.register(Feature)
class FeatureAdmin(admin.ModelAdmin):
    list_display = ('title', 'section', 'order')
    list_filter = ('section',)
    ordering = ('section', 'order')


@admin.register(Announcement)
class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'is_published')
    list_filter = ('is_published',)
    search_fields = ('title',)


@admin.register(ContactInfo)
class ContactInfoAdmin(admin.ModelAdmin):
    list_display = ('email', 'phone', 'is_active')


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('name', 'role', 'rating', 'is_active')
    list_filter = ('is_active',)


@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ('question', 'order', 'is_active')
    list_filter = ('is_active',)
