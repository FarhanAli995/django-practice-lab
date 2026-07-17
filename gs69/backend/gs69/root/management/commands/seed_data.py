from django.core.management.base import BaseCommand
from root.models import UserProfile

class Command(BaseCommand):
    help = 'Seed the database with sample user profiles'

    def handle(self, *args, **options):
        sample_data = [
            {
                'name': 'John Doe',
                'email': 'john@example.com',
                'mobile_number': '1234567890',
                'education': 'Bachelor',
                'profession': 'Developer',
                'company': 'Tech Corp',
                'experience_years': 5,
                'is_active': True
            },
            {
                'name': 'Jane Smith',
                'email': 'jane@example.com',
                'mobile_number': '9876543210',
                'education': 'Master',
                'profession': 'Designer',
                'company': 'Design Studio',
                'experience_years': 3,
                'is_active': True
            },
            {
                'name': 'Bob Johnson',
                'email': 'bob@example.com',
                'mobile_number': '5551234567',
                'education': 'PhD',
                'profession': 'Researcher',
                'company': 'Research Lab',
                'experience_years': 8,
                'is_active': False
            },
            {
                'name': 'Alice Brown',
                'email': 'alice@example.com',
                'mobile_number': '4449876543',
                'education': 'Bachelor',
                'profession': 'Manager',
                'company': 'Business Inc',
                'experience_years': 7,
                'is_active': True
            },
            {
                'name': 'David Wilson',
                'email': 'david@example.com',
                'mobile_number': '3335557777',
                'education': 'Master',
                'profession': 'Engineer',
                'company': 'Engineering Co',
                'experience_years': 10,
                'is_active': True
            },
            {
                'name': 'Emma Garcia',
                'email': 'emma@example.com',
                'mobile_number': '2224448888',
                'education': 'Bachelor',
                'profession': 'Consultant',
                'company': 'Consulting Group',
                'experience_years': 4,
                'is_active': False
            }
        ]

        created_count = 0
        for data in sample_data:
            profile, created = UserProfile.objects.get_or_create(
                email=data['email'],
                defaults=data
            )
            if created:
                created_count += 1
                self.stdout.write(self.style.SUCCESS(f'Created: {profile.name}'))
            else:
                self.stdout.write(self.style.WARNING(f'Skipped (already exists): {profile.name}'))

        self.stdout.write(self.style.SUCCESS(f'Successfully created {created_count} new profiles'))
