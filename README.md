# Fourth Quarter Cigar (4QC) Website

Official website for the indie pop/rock band Fourth Quarter Cigar.

## Features

- **Home Page**: Full-screen video background, merch carousel, releases showcase, band members, and upcoming shows
- **Music Page**: Complete discography with streaming links to Spotify and YouTube
- **Shows Page**: Upcoming and past concert listings with setlists
- **Responsive Design**: Fully optimized for desktop, tablet, and mobile devices

## Technology Stack

- Django 5.2.8
- Python 3.11
- HTML5/CSS3
- JavaScript

## Setup

1. Clone the repository:
```bash
git clone https://github.com/princeellis/fourthquartercigar.git
cd fourthquartercigar
```

2. Create and activate a virtual environment:
```bash
python -m venv 4QCenv
source 4QCenv/bin/activate  # On Windows: 4QCenv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run migrations:
```bash
python manage.py migrate
```

5. Create a superuser:
```bash
python manage.py createsuperuser
```

6. Populate initial data (optional):
```bash
python manage.py populate_data
```

7. Run the development server:
```bash
python manage.py runserver
```

## Admin Panel

Access the Django admin panel at `http://127.0.0.1:8000/admin/` to manage:
- Band members
- Releases and songs
- Concerts and concert photos
- Band photos
- Merch photos

## Project Structure

```
fqcproj/
├── base/              # Main Django app
│   ├── models.py      # Database models
│   ├── views.py       # View functions
│   ├── admin.py       # Admin configuration
│   ├── templates/     # HTML templates
│   └── static/        # CSS, images, videos
├── fqcproj/           # Django project settings
│   ├── settings.py    # Project configuration
│   └── urls.py        # URL routing
└── manage.py          # Django management script
```

## Media Files

Upload images and videos through the Django admin panel. Media files are stored in the `media/` directory.

## Static Files

Static files (CSS, images, videos) are located in `base/static/base/`. Run `python manage.py collectstatic` to collect static files for production.

## License

All rights reserved.
