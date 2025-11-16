from django.core.management.base import BaseCommand
from django.utils import timezone
from datetime import date
from base.models import Concert

class Command(BaseCommand):
    help = 'Add the first concert at Rock Bible Church'

    def add_arguments(self, parser):
        parser.add_argument(
            '--date',
            type=str,
            help='Concert date in YYYY-MM-DD format (e.g., 2025-01-15)',
        )

    def handle(self, *args, **options):
        # Get date from argument or ask user
        if options['date']:
            try:
                concert_date = date.fromisoformat(options['date'])
            except ValueError:
                self.stdout.write(self.style.ERROR('Invalid date format. Use YYYY-MM-DD'))
                return
        else:
            # Default to today if no date provided (you can change this)
            concert_date = date.today()
            self.stdout.write(self.style.WARNING(f'No date provided. Using today: {concert_date}'))
            self.stdout.write(self.style.WARNING('To specify a date, use: --date YYYY-MM-DD'))
        
        setlist = "Need a Ride, End of Beginning (Djo), Valerie (Amy W), Relax (Vacations), Away, Show Me How (Men I Trust), Doomsday (Lizzy M), Not This Time"
        
        concert, created = Concert.objects.get_or_create(
            venue='Rock Bible Church',
            city='Pleasanton',
            state='CA',
            defaults={
                'date': concert_date,
                'is_upcoming': False,  # Past concert
                'setlist': setlist,
            }
        )
        
        if created:
            self.stdout.write(self.style.SUCCESS(f'Successfully added concert: {concert}'))
            self.stdout.write(self.style.SUCCESS(f'Setlist: {setlist}'))
            self.stdout.write(self.style.WARNING('Remember to add the concert photo through the admin panel!'))
        else:
            self.stdout.write(self.style.WARNING(f'Concert already exists: {concert}'))
            # Update setlist if it exists
            if not concert.setlist:
                concert.setlist = setlist
                concert.save()
                self.stdout.write(self.style.SUCCESS('Updated setlist'))

