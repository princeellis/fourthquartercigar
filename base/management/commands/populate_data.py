from django.core.management.base import BaseCommand
from django.utils import timezone
from datetime import date
from base.models import BandMember, Release, Song

class Command(BaseCommand):
    help = 'Populate database with initial band data'

    def handle(self, *args, **options):
        # Only populate if database is empty (first time setup)
        if BandMember.objects.exists() or Release.objects.exists():
            self.stdout.write(self.style.WARNING('Database already populated. Skipping...'))
            return
        
        # Create band members
        members_data = [
            {'name': 'Elisha (Eli) McDuffie', 'role': 'Electric Guitar', 'instagram_handle': 'elishamcduffie', 'order': 1},
            {'name': 'Micah McDuffie', 'role': 'Drums', 'instagram_handle': None, 'order': 2},
            {'name': 'Katie Berglin', 'role': 'Singer', 'instagram_handle': 'katie.berglin', 'order': 3},
            {'name': 'Coleson Franklin', 'role': 'Bass Guitar', 'instagram_handle': 'colesonfranklin_', 'order': 4},
            {'name': 'Austin Martin', 'role': 'Electric Guitar and Singer', 'instagram_handle': None, 'order': 5},
            {'name': 'Carter Randell', 'role': 'Bass Guitar', 'instagram_handle': 'cjrandell0', 'order': 6},
        ]
        
        for member_data in members_data:
            BandMember.objects.create(**member_data)
        
        self.stdout.write(self.style.SUCCESS('Created band members'))
        
        # Create Passenger EP
        passenger_ep = Release.objects.create(
            title='Passenger',
            release_type='EP',
            release_date=date(2025, 1, 1),
            spotify_url='https://open.spotify.com/album/1kZvNHfYfRCMY1XChAZSkv?si=0ajwpIB5QZKyRPV-u2V2gQ',
            youtube_url='https://youtube.com/playlist?list=OLAK5uy_kA_WGaQdtHILnPbosmf_fJe6DLEYaAyDM&si=b89W4NCgvQsotbtc',
            order=1
        )
        
        # Create songs for Passenger EP
        songs_data = [
            {
                'title': 'Away',
                'spotify_url': 'https://open.spotify.com/track/6ff6j4s5E2ABOKA9ogOJwG?si=a7a889256fa64a11',
                'youtube_url': 'https://www.youtube.com/watch?v=3claX2MmHsY&list=OLAK5uy_mASAuiqOZE2Gj4IIACpN9j5JC_fh3nqxI',
                'track_number': 1,
                'duration': '4:10',
                'streams': 6432
            },
            {
                'title': 'Need a Ride',
                'spotify_url': 'https://open.spotify.com/track/3HSePZ7a9MKGFoCRaaSyF2?si=9981bd27f78d485e',
                'youtube_url': 'https://www.youtube.com/watch?v=cM9WgsBiIZQ&list=OLAK5uy_mvFz2FzgWF-jR0REGZ3pHXZUkKOvMRnIo',
                'track_number': 2,
                'duration': '3:22',
                'streams': 0
            },
            {
                'title': 'Without Her',
                'spotify_url': 'https://open.spotify.com/track/3vgVL7Bl7yruUJgTmsOdCi?si=99471a76a9bd4160',
                'youtube_url': 'https://youtu.be/gujBn4-hBQE?si=UljNSz1vvdEwbvpy',
                'track_number': 3,
                'duration': '3:23',
                'streams': 0
            },
            {
                'title': 'Passenger',
                'spotify_url': 'https://open.spotify.com/track/125HJZB1iuXs9fPAVQtj6o?si=1552e49c9b534ce0',
                'youtube_url': 'https://youtu.be/TUGTtAgo0Pg?si=M7hYeBz_kw31YP7K',
                'track_number': 4,
                'duration': '3:58',
                'streams': 0
            },
            {
                'title': 'Not This Time',
                'spotify_url': 'https://open.spotify.com/track/15WV6JpLu80ZzXLbqpfMOd?si=1211a1c4777244ae',
                'youtube_url': 'https://youtu.be/IGC7Rf_Rl6s?si=to-CzVkZIi9Wcczx',
                'track_number': 5,
                'duration': '4:15',
                'streams': 0
            },
        ]
        
        for song_data in songs_data:
            Song.objects.create(release=passenger_ep, **song_data)
        
        self.stdout.write(self.style.SUCCESS('Created Passenger EP and songs'))
        
        # Create Away single
        away_single = Release.objects.create(
            title='Away',
            release_type='Single',
            release_date=date(2025, 1, 1),
            spotify_url='https://open.spotify.com/track/6ff6j4s5E2ABOKA9ogOJwG?si=a7a889256fa64a11',
            youtube_url='https://www.youtube.com/watch?v=3claX2MmHsY&list=OLAK5uy_mASAuiqOZE2Gj4IIACpN9j5JC_fh3nqxI',
            order=2
        )
        
        Song.objects.create(
            release=away_single,
            title='Away',
            spotify_url='https://open.spotify.com/track/6ff6j4s5E2ABOKA9ogOJwG?si=a7a889256fa64a11',
            youtube_url='https://www.youtube.com/watch?v=3claX2MmHsY&list=OLAK5uy_mASAuiqOZE2Gj4IIACpN9j5JC_fh3nqxI',
            track_number=1,
            duration='4:10',
            streams=6432
        )
        
        # Create Need a Ride single
        need_a_ride_single = Release.objects.create(
            title='Need a Ride',
            release_type='Single',
            release_date=date(2025, 1, 1),
            spotify_url='https://open.spotify.com/track/3HSePZ7a9MKGFoCRaaSyF2?si=9981bd27f78d485e',
            youtube_url='https://www.youtube.com/watch?v=cM9WgsBiIZQ&list=OLAK5uy_mvFz2FzgWF-jR0REGZ3pHXZUkKOvMRnIo',
            order=3
        )
        
        Song.objects.create(
            release=need_a_ride_single,
            title='Need a Ride',
            spotify_url='https://open.spotify.com/track/3HSePZ7a9MKGFoCRaaSyF2?si=9981bd27f78d485e',
            youtube_url='https://www.youtube.com/watch?v=cM9WgsBiIZQ&list=OLAK5uy_mvFz2FzgWF-jR0REGZ3pHXZUkKOvMRnIo',
            track_number=1,
            duration='3:22',
            streams=0
        )
        
        self.stdout.write(self.style.SUCCESS('Created singles'))
        self.stdout.write(self.style.SUCCESS('Successfully populated database!'))

