from django.http import HttpResponsePermanentRedirect, HttpResponseNotFound, HttpResponseBadRequest
from django.core.files.storage import default_storage
from easy_thumbnails.files import get_thumbnailer
from easy_thumbnails.exceptions import InvalidImageFormatError
import re


SIZE_RE = re.compile(r'^(\d+),(\d+)$')


def resize(path,size=None,crop=None):
    thumbnail_opts = {}
    if size:
        if SIZE_RE.match(size):
            thumbnail_opts['size'] = tuple(map(int, size.split(',')))
            if crop:
                thumbnail_opts['crop'] = crop
        else:
            return default_storage.url(path)
    else:
        return default_storage.url(path)
    try:
        thumbnailer = get_thumbnailer(default_storage, path)
        thumbnail = thumbnailer.get_thumbnail(thumbnail_opts)
        return thumbnail.url
        #return HttpResponsePermanentRedirect(thumbnail.url)
    except IOError:
        return False
    except InvalidImageFormatError:
        return False