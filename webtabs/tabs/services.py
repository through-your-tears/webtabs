from django.core.files import File
from bs4 import BeautifulSoup
import requests as r

from .repositories import WebTagRepository


def get_ogp(url: str, author):
    try:
        res = r.get(url)
    except r.exceptions.ConnectionError:
        return
    if res.status_code < 300:
        soup = BeautifulSoup(res.text, 'html.parser')
        title = soup.title.text
        try:
            url_type = soup.find('meta', attrs={'property': 'og:type'})['content']
        except TypeError:
            url_type = 'website'
        try:
            image_url = soup.find('meta', attrs={'property': 'og:image'})['content']
            img = r.get(image_url)
            filepath = title.replace(' ', '_')
            filepath = filepath[:8] + '.jpg'
            with open(filepath, 'wb') as f:
                f.write(img.content)
        except Exception:
            img = None
            filepath = ''
        try:
            description = soup.find('meta', attrs={'property': 'og:description'})['content']
        except TypeError:
            description = None
        if img:
            with open(filepath, 'rb') as f:
                image = File(f)
                return WebTagRepository.add({
                    'title': title,
                    'url_type': url_type,
                    'image': image,
                    'description': description,
                    'author': author,
                    'url': url
                })
        else:
            return WebTagRepository.add({
                'title': title,
                'url_type': url_type,
                'image': None,
                'description': description,
                'author': author,
                'url': url
            })
    else:
        return
