from django.core.management.base import BaseCommand
from datetime import date
from base.models import Release, Concert, MerchPhoto

class Command(BaseCommand):
    help = 'Update existing records to use static image URLs'

    def handle(self, *args, **options):
        # Update Passenger EP artwork
        try:
            passenger = Release.objects.get(title='Passenger', release_type='EP')
            passenger.artwork_url = '/static/base/images/artwork/passenger.JPG'
            passenger.save()
            self.stdout.write(self.style.SUCCESS('Updated Passenger EP artwork'))
        except Release.DoesNotExist:
            self.stdout.write(self.style.WARNING('Passenger EP not found'))
        
        # Update Away single artwork
        try:
            away = Release.objects.get(title='Away', release_type='Single')
            away.artwork_url = '/static/base/images/artwork/away.jpg'
            away.save()
            self.stdout.write(self.style.SUCCESS('Updated Away single artwork'))
        except Release.DoesNotExist:
            self.stdout.write(self.style.WARNING('Away single not found'))
        
        # Update Need a Ride single artwork
        try:
            need_a_ride = Release.objects.get(title='Need a Ride', release_type='Single')
            need_a_ride.artwork_url = '/static/base/images/artwork/needaride.JPEG'
            need_a_ride.save()
            self.stdout.write(self.style.SUCCESS('Updated Need a Ride single artwork'))
        except Release.DoesNotExist:
            self.stdout.write(self.style.WARNING('Need a Ride single not found'))
        
        # Update or create RBC concert
        rbc, created = Concert.objects.get_or_create(
            venue='Rock Bible Church',
            city='Pleasanton',
            defaults={
                'date': date(2024, 11, 1),
                'state': 'CA',
                'is_upcoming': False,
                'photo_url': '/static/base/images/concerts/RBC.JPG',
                'setlist': 'Need a Ride, End of Beginning (Djo), Valerie (Amy Winehouse), Relax (Vacations), Away, Show Me How (Men I Trust), Doomsday (Lizzy McAlpine), Not This Time'
            }
        )
        if not created:
            rbc.photo_url = '/static/base/images/concerts/RBC.JPG'
            rbc.save()
        self.stdout.write(self.style.SUCCESS(f'{"Created" if created else "Updated"} RBC concert'))
        
        # Create merch photos if they don't exist
        merch_data = [
            {'caption': 'Passenger EP T-Shirt', 'photo_url': '/static/base/images/merch/passenger-ep-t-shirt-Picsart-BackgroundRemover.jpg', 'order': 1},
            {'caption': 'Geese Madness T-Shirt', 'photo_url': '/static/base/images/merch/geese-madness-t-shirt-Picsart-BackgroundRemover.jpg', 'order': 2},
            {'caption': 'Need a Ride Crew', 'photo_url': '/static/base/images/merch/need-a-ride-catherine-assisted-ad-crew-Picsart-BackgroundRemover.jpg', 'order': 3},
            {'caption': 'Cigar Logo Trucker Cap', 'photo_url': '/static/base/images/merch/fourth-quarter-cigar-cigar-logo-trucker-cap-Picsart-BackgroundRemover.jpg', 'order': 4},
        ]
        
        for merch in merch_data:
            obj, created = MerchPhoto.objects.get_or_create(
                caption=merch['caption'],
                defaults=merch
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Created merch: {merch["caption"]}'))
        
        self.stdout.write(self.style.SUCCESS('Successfully updated all static images!'))

