from django.contrib import admin
from .models import BandMember, Release, Song, Concert, ConcertPhoto, BandPhoto, MerchPhoto

@admin.register(BandMember)
class BandMemberAdmin(admin.ModelAdmin):
    list_display = ['name', 'role', 'instagram_handle', 'order']
    list_editable = ['order']

@admin.register(Release)
class ReleaseAdmin(admin.ModelAdmin):
    list_display = ['title', 'release_type', 'release_date', 'order']
    list_editable = ['order']
    inlines = []

@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ['title', 'release', 'track_number', 'streams']
    list_filter = ['release']

class ConcertPhotoInline(admin.TabularInline):
    model = ConcertPhoto
    extra = 1
    fields = ('photo', 'photo_url', 'caption', 'order')

@admin.register(Concert)
class ConcertAdmin(admin.ModelAdmin):
    list_display = ['date', 'venue', 'city', 'state', 'is_upcoming']
    list_filter = ['is_upcoming', 'date']
    date_hierarchy = 'date'
    inlines = [ConcertPhotoInline]
    fieldsets = (
        ('Concert Details', {
            'fields': ('date', 'venue', 'city', 'state', 'is_upcoming', 'ticket_url')
        }),
        ('Content', {
            'fields': ('setlist', 'photo', 'photo_url')
        }),
    )

@admin.register(ConcertPhoto)
class ConcertPhotoAdmin(admin.ModelAdmin):
    list_display = ['concert', 'caption', 'order']
    list_filter = ['concert']
    list_editable = ['order']

@admin.register(BandPhoto)
class BandPhotoAdmin(admin.ModelAdmin):
    list_display = ['caption', 'is_hero', 'is_music_header', 'is_shows_header', 'order']
    list_editable = ['is_hero', 'is_music_header', 'is_shows_header', 'order']
    list_filter = ['is_hero', 'is_music_header', 'is_shows_header']

@admin.register(MerchPhoto)
class MerchPhotoAdmin(admin.ModelAdmin):
    list_display = ['caption', 'order']
    list_editable = ['order']
