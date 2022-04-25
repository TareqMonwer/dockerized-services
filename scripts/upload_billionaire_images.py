from django.core.files.base import ContentFile
from core.models import Millionaire


IMAGE_API_URL = "https://random.imagecdn.app/400/400"

millionaires = Millionaire.objects.all()

def run():
    for millionaire in millionaires:
        print(millionaire.name)
