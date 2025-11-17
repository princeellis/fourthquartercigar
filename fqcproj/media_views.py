from django.http import FileResponse, Http404
from django.conf import settings
import os

def serve_media(request, path):
    """
    Serve media files in production.
    This bypasses Django's DEBUG requirement for serving files.
    """
    file_path = os.path.join(settings.MEDIA_ROOT, path)
    
    if not os.path.exists(file_path):
        raise Http404("Media file not found")
    
    return FileResponse(open(file_path, 'rb'))

