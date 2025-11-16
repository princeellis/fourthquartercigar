# Fourth Quarter Cigar Website

A Django website for the indie rock/pop band Fourth Quarter Cigar (4QC).

## Features

- **Home Page**: Band introduction, members, latest releases, and upcoming concerts
- **Music Page**: All releases (EP and singles) with Spotify and YouTube links
- **Concerts Page**: Upcoming and past shows
- **Contact Page**: Contact form and social media links
- **Merch Link**: Direct link to Printify store
- **Admin Panel**: Manage band members, releases, songs, and concerts

## Setup

1. **Activate the virtual environment:**
   ```bash
   cd fqcproj
   source 4QCenv/bin/activate
   ```

2. **Run migrations (already done):**
   ```bash
   python manage.py migrate
   ```

3. **Populate initial data (already done):**
   ```bash
   python manage.py populate_data
   ```

4. **Create a superuser for admin access:**
   ```bash
   python manage.py createsuperuser
   ```

5. **Run the development server:**
   ```bash
   python manage.py runserver
   ```

6. **Access the site:**
   - Website: http://127.0.0.1:8000/
   - Admin: http://127.0.0.1:8000/admin/

## Managing Content

### Adding Concert Dates

1. Go to http://127.0.0.1:8000/admin/
2. Log in with your superuser account
3. Click on "Concerts" → "Add Concert"
4. Fill in:
   - Date
   - Venue
   - City
   - State (optional)
   - Ticket URL (optional)
   - Check "Is upcoming" for future shows

### Adding New Releases

1. Go to Admin → "Releases" → "Add Release"
2. Fill in release details
3. Add songs to the release by going to "Songs" → "Add Song" and selecting the release

### Updating Band Members

1. Go to Admin → "Band Members"
2. Edit existing members or add new ones
3. Use the "Order" field to control display order

## Color Scheme

The site uses colors from the band logo:
- **Dark Gray** (#4a4a4a): "FOURTH"
- **Rusty Red** (#c45a3a): "QUARTER"
- **Muted Blue/Teal** (#4a7c7e): "CIGAR"
- **Black**: Backgrounds and navigation

## Current Data

- **Band Members**: 6 members (Eli, Micah, Katie, Coleson, Austin, Carter)
- **Releases**: 
  - Passenger EP (5 songs)
  - Away (Single)
  - Need a Ride (Single)
- **Social Links**: Spotify, YouTube, Instagram
- **Merch**: Printify store link

## Notes

- The contact form currently sends emails to the console (for development). Update `EMAIL_BACKEND` in `settings.py` for production.
- Concert dates can be added through the admin panel as they become available.
- All Spotify and YouTube links are already configured.

