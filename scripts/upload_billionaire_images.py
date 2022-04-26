"""Upload images for millioanires who has no image attached yet."""
import multiprocessing
import requests
from django.core.files import File
from django.core.files.temp import NamedTemporaryFile
from core.models import Millionaire


IMAGE_API_URL = "https://random.imagecdn.app/400/400"

millionaires = Millionaire.objects.all()

def update_image(millionaire):
    if not millionaire.image:
        r = requests.get(IMAGE_API_URL)
        img_temp = NamedTemporaryFile(delete=True)
        img_temp.write(r.content)
        img_temp.flush()

        millionaire.image.save(
            f"{millionaire.name}-{millionaire.id}.jpg", File(img_temp), 
            save=True
        )


def run():
    p = multiprocessing.Pool(50)
    p.map(update_image, millionaires)
    p.close()
    p.join()