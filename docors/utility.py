# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.gis.geoip import GeoIP
import re

# this is not intended to be an all-knowing IP address regex
IP_RE = re.compile('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')


def get_ip(request):
    """
    Retrieves the remote IP address from the request data.  If the user is
    behind a proxy, they may have a comma-separated list of IP addresses, so
    we need to account for that.  In such a case, only the first IP in the
    list will be retrieved.  Also, some hosts that use a proxy will put the
    REMOTE_ADDR into HTTP_X_FORWARDED_FOR.  This will handle pulling back the
    IP from the proper place.

    **NOTE** This function was taken from django-tracking (MIT LICENSE)
             http://code.google.com/p/django-tracking/
    """

    # if neither header contain a value, just use local loopback
    ip_address = request.META.get('HTTP_X_FORWARDED_FOR',
                                  request.META.get('REMOTE_ADDR', '127.0.0.1'))
    if ip_address:
        # make sure we have one and only one IP
        try:
            ip_address = IP_RE.match(ip_address)
            if ip_address:
                ip_address = ip_address.group(0)
            else:
                # no IP, probably from some dirty proxy or other device
                # throw in some bogus IP
                ip_address = '10.0.0.1'
        except IndexError:
            pass

    return ip_address

def get_city(request):
	user_ip = get_ip(request)
	g = GeoIP()
	city_info = g.city(user_ip)
	if city_info is not None:
		return city_info['city']
	else:
		return 'lahore'

def get_lat_lon(request):
    user_ip = get_ip(request)
    g = GeoIP()
    lat_lon = g.lat_lon(user_ip)
    if lat_lon is not None:
        return lat_lon
    else:
        return (31.519191, 74.326237)
