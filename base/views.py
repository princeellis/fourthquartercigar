from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from django.utils import timezone
from django.views.decorators.http import require_http_methods
from .models import BandMember, Release, Song, Concert, ConcertPhoto, BandPhoto, MerchPhoto

def home(request):
    members = BandMember.objects.all()
    # Clean up member names to remove "(Eli)"
    for member in members:
        if "(Eli)" in member.name:
            member.display_name = member.name.replace("(Eli)", "").replace("Elisha  ", "Elisha ").strip()
        else:
            member.display_name = member.name
    
    releases = Release.objects.all().order_by('-order', '-release_date')
    upcoming_concerts = Concert.objects.filter(is_upcoming=True, date__gte=timezone.now().date()).prefetch_related('photos')
    hero_photo = BandPhoto.objects.filter(is_hero=True).first()
    band_photos = BandPhoto.objects.all()[:6]  # Get up to 6 photos for gallery
    merch_photos = MerchPhoto.objects.all()
    
    context = {
        'members': members,
        'releases': releases,
        'upcoming_concerts': upcoming_concerts,
        'hero_photo': hero_photo,
        'band_photos': band_photos,
        'merch_photos': merch_photos,
        'merch_url': 'https://fourth-quarter-cigar.printify.me/',
        'spotify_artist_url': 'https://open.spotify.com/artist/56R16YVbAr8n52dHnTlN3W?si=WraFGgyrQy-we3lYrcfsjg',
        'instagram_handle': 'fourthquartercigar',
        'youtube_channel_url': 'https://www.youtube.com/channel/UCtMhupPWuqEgjAlZEsrr8rQ',
    }
    return render(request, 'base/home.html', context)

def music(request):
    releases = Release.objects.all()
    band_photos = list(BandPhoto.objects.all())
    import random
    random.shuffle(band_photos)  # Randomize order
    # Create a list of photo indices to use between releases
    photo_indices = []
    for i in range(len(releases) * 2):  # One before and one after each release
        if band_photos:
            photo_indices.append(i % len(band_photos))
    members = BandMember.objects.all()
    # Clean up member names to remove "(Eli)"
    for member in members:
        if "(Eli)" in member.name:
            member.display_name = member.name.replace("(Eli)", "").replace("Elisha  ", "Elisha ").strip()
        else:
            member.display_name = member.name
    context = {
        'releases': releases,
        'spotify_artist_url': 'https://open.spotify.com/artist/56R16YVbAr8n52dHnTlN3W?si=WraFGgyrQy-we3lYrcfsjg',
        'band_photos': band_photos,
        'photo_indices': photo_indices,
        'members': members,
    }
    return render(request, 'base/music.html', context)

def concerts(request):
    upcoming = Concert.objects.filter(is_upcoming=True, date__gte=timezone.now().date()).prefetch_related('photos')
    past = Concert.objects.filter(is_upcoming=False).order_by('-date')[:10].prefetch_related('photos')
    band_photos = list(BandPhoto.objects.all())
    import random
    random.shuffle(band_photos)  # Randomize order
    # Create a list of photo indices to use between concerts
    total_concerts = len(upcoming) + len(past)
    photo_indices = []
    for i in range(total_concerts * 2):  # One before and one after each concert
        if band_photos:
            photo_indices.append(i % len(band_photos))
    members = BandMember.objects.all()
    # Clean up member names to remove "(Eli)"
    for member in members:
        if "(Eli)" in member.name:
            member.display_name = member.name.replace("(Eli)", "").replace("Elisha  ", "Elisha ").strip()
        else:
            member.display_name = member.name
    
    context = {
        'upcoming_concerts': upcoming,
        'past_concerts': past,
        'band_photos': band_photos,
        'photo_indices': photo_indices,
        'members': members,
    }
    return render(request, 'base/concerts.html', context)

@require_http_methods(["GET", "POST"])
def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        message = request.POST.get('message', '')
        
        if name and email and message:
            try:
                send_mail(
                    subject=f'Contact from {name} - 4QC Website',
                    message=f'From: {name} ({email})\n\n{message}',
                    from_email=settings.DEFAULT_FROM_EMAIL if hasattr(settings, 'DEFAULT_FROM_EMAIL') else email,
                    recipient_list=['fourthquartercigar@gmail.com'],
                    fail_silently=False,
                )
                messages.success(request, 'Thank you! Your message has been sent.')
            except Exception as e:
                messages.error(request, 'Sorry, there was an error sending your message. Please try again.')
        else:
            messages.error(request, 'Please fill in all fields.')
    
    return render(request, 'base/contact.html')
