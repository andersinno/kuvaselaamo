# -*- coding: utf-8 -*-

import logging
import urllib
import urlparse
from StringIO import StringIO

import requests
from PIL import Image

from django.core.cache import cache


LOG = logging.getLogger(__name__)


class HKMClient(object):
    timeout = 6

    def get_full_res_image_url(self, preview_image_url):
        """
        HKM image server responds with 200 text body response if there is no full res version for the
        image. This checks the response headers to find out whether full res image exists or not and
        returns the full res image url if it does. Else returns None
        """
        cache_key = 'hkm_%s' % preview_image_url
        cached_value = cache.get(cache_key)
        if cached_value:
            return cached_value

        url_components = urlparse.urlparse(preview_image_url)
        qs_params = dict(urlparse.parse_qsl(url_components.query))
        qs_params['dataType'] = 'org'

        url_components = list(url_components)
        url_components[4] = urllib.urlencode(qs_params)
        url = urlparse.urlunparse(url_components)
        try:
            r = requests.head(url, timeout=self.timeout)
        except requests.exceptions.RequestException:
            LOG.error('Failed to communicate with HKM image server',
                      exc_info=True)
            # Cache negative result for an hour
            cache.set(cache_key, None, 3600)
            return None
        else:
            try:
                r.raise_for_status()
                # raise requests.exceptions.HTTPError()
            except requests.exceptions.HTTPError:
                LOG.error('Failed to communicate with HKM image server', exc_info=True,
                          extra={'data': {'status_code': r.status_code, 'response': repr(r.text)}})
                # Cache negative result for an hour
                cache.set(cache_key, None, 3600)
                return None

        LOG.debug('Got result from HKM image server',
                  extra={'data': {'url': url, 'result_headers': repr(r.headers)}})
        try:
            content_type = r.headers['content-type']
            if 'image' in content_type:
                # Cache positive result for a week
                cache.set(cache_key, url, 7 * 24 * 3600)
                return url
        except KeyError:
            pass

        cache.set(cache_key, None, 3600)
        return None

    def download_image(self, full_res_url):
        r = requests.get(full_res_url, stream=True)
        try:
            r.raise_for_status()
        except requests.exceptions.RequestException:
            LOG.error('Could not download a full res url',
                      extra={'data': {'img_url': full_res_url}})
        else:
            return Image.open(StringIO(r.content))
        return None


DEFAULT_CLIENT = HKMClient()


