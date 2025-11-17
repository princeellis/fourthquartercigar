from django.db import models

class BandMember(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=200, help_text="e.g., Electric Guitar, Drums, Singer")
    instagram_handle = models.CharField(max_length=100, blank=True, null=True, help_text="Without @ symbol")
    order = models.IntegerField(default=0, help_text="Display order")
    
    class Meta:
        ordering = ['order', 'name']
    
    def __str__(self):
        return self.name

class Release(models.Model):
    RELEASE_TYPE_CHOICES = [
        ('EP', 'EP'),
        ('Single', 'Single'),
        ('Album', 'Album'),
    ]
    
    title = models.CharField(max_length=200)
    release_type = models.CharField(max_length=20, choices=RELEASE_TYPE_CHOICES)
    release_date = models.DateField()
    spotify_url = models.URLField()
    youtube_url = models.URLField(blank=True, null=True)
    artwork = models.ImageField(upload_to='artwork/', blank=True, null=True, help_text="Upload artwork image")
    artwork_url = models.URLField(blank=True, null=True, help_text="Or provide URL to artwork image")
    order = models.IntegerField(default=0, help_text="Display order (newest first)")
    
    def get_artwork_url(self):
        """Return artwork URL from file upload or URL field"""
        # Prioritize photo_url if provided
        if self.artwork_url:
            return self.artwork_url
        # Fall back to uploaded file if it exists
        if self.artwork:
            return self.artwork.url
        return None
    
    class Meta:
        ordering = ['-order', '-release_date']
    
    def __str__(self):
        return f"{self.title} ({self.release_type})"

class Song(models.Model):
    title = models.CharField(max_length=200)
    release = models.ForeignKey(Release, on_delete=models.CASCADE, related_name='songs')
    spotify_url = models.URLField()
    youtube_url = models.URLField(blank=True, null=True)
    track_number = models.IntegerField(default=1)
    duration = models.CharField(max_length=20, blank=True, help_text="e.g., 4:10")
    streams = models.IntegerField(default=0, help_text="Stream count")
    
    class Meta:
        ordering = ['release', 'track_number']
    
    def __str__(self):
        return f"{self.title} - {self.release.title}"

class Concert(models.Model):
    date = models.DateField()
    venue = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=50, blank=True)
    ticket_url = models.URLField(blank=True, null=True)
    is_upcoming = models.BooleanField(default=True)
    setlist = models.TextField(blank=True, null=True, help_text="Setlist for the show")
    # Keep single photo for backward compatibility/main photo
    photo = models.ImageField(upload_to='concerts/', blank=True, null=True, help_text="Main concert photo")
    photo_url = models.URLField(blank=True, null=True, help_text="Or provide URL to main concert photo")
    
    class Meta:
        ordering = ['date']
    
    def get_photo_url(self):
        """Return photo URL from file upload or URL field"""
        # Prioritize photo_url if provided
        if self.photo_url:
            return self.photo_url
        # Fall back to uploaded file if it exists
        if self.photo:
            return self.photo.url
        return None
    
    def __str__(self):
        location = f"{self.city}, {self.state}" if self.state else self.city
        return f"{self.venue} - {location} ({self.date})"

class ConcertPhoto(models.Model):
    concert = models.ForeignKey(Concert, on_delete=models.CASCADE, related_name='photos')
    photo = models.ImageField(upload_to='concerts/', help_text="Concert photo")
    photo_url = models.URLField(blank=True, null=True, help_text="Or provide URL to photo")
    caption = models.CharField(max_length=200, blank=True, null=True)
    order = models.IntegerField(default=0, help_text="Display order")
    
    class Meta:
        ordering = ['order', 'id']
    
    def get_photo_url(self):
        """Return photo URL from file upload or URL field"""
        # Prioritize photo_url if provided
        if self.photo_url:
            return self.photo_url
        # Fall back to uploaded file if it exists
        if self.photo:
            return self.photo.url
        return None
    
    def __str__(self):
        return f"{self.concert.venue} - Photo {self.id}"

class BandPhoto(models.Model):
    photo = models.ImageField(upload_to='band_photos/', help_text="Band photo")
    photo_url = models.URLField(blank=True, null=True, help_text="Or provide URL to photo")
    caption = models.CharField(max_length=200, blank=True, null=True)
    is_hero = models.BooleanField(default=False, help_text="Use as hero image on home page")
    is_music_header = models.BooleanField(default=False, help_text="Use as header image on music page")
    is_shows_header = models.BooleanField(default=False, help_text="Use as header image on shows page")
    order = models.IntegerField(default=0, help_text="Display order")
    
    class Meta:
        ordering = ['-is_hero', 'order']
    
    def get_photo_url(self):
        """Return photo URL from file upload or URL field"""
        # Prioritize photo_url if provided
        if self.photo_url:
            return self.photo_url
        # Fall back to uploaded file if it exists
        if self.photo:
            return self.photo.url
        return None
    
    def __str__(self):
        return self.caption or f"Band Photo {self.id}"

class MerchPhoto(models.Model):
    photo = models.ImageField(upload_to='merch/', help_text="Merch photo")
    photo_url = models.URLField(blank=True, null=True, help_text="Or provide URL to photo")
    caption = models.CharField(max_length=200, blank=True, null=True, help_text="Product name or description")
    order = models.IntegerField(default=0, help_text="Display order")
    
    class Meta:
        ordering = ['order', 'id']
    
    def get_photo_url(self):
        """Return photo URL from file upload or URL field"""
        # Prioritize photo_url if provided
        if self.photo_url:
            return self.photo_url
        # Fall back to uploaded file if it exists
        if self.photo:
            return self.photo.url
        return None
    
    def __str__(self):
        return self.caption or f"Merch Photo {self.id}"
