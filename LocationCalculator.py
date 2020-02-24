import math

EARTH_RADIO_KM = 6378.137


class GeoLocationBox:
    """This class stores latitude and longitude for a box four sides"""
    def __init__(self, left, top, right, bottom):
        self.left = left
        self.top = top
        self.right = right
        self.bottom = bottom

    def is_in_box(self, lat, lng):
        """Check if the (lat, lng) in in the box, return True or False"""
        is_between_horizontal = self.right >= lat >= self.left
        is_between_vertical = self.top >= lng >= self.bottom
        coord_is_in_box = is_between_horizontal and is_between_vertical
        print('IsInBox ({},{})? {}'.format(lat, lng, coord_is_in_box))
        return coord_is_in_box


def add_meters_to_latitude(latitude, distance_meters):
    """Add a distance in meters(distance_meters) to a latitude(latitude) and return new latitude"""
    m = (1 / ((2 * math.pi / 360) * EARTH_RADIO_KM)) / 1000
    return latitude + (distance_meters * m)


def add_meters_to_longitude(longitude, latitude, distance_meters):
    """Add a distance in meters(distance_meters) to a longitude(longitude) and return new longitude"""
    m = (1 / ((2 * math.pi / 360) * EARTH_RADIO_KM)) / 1000
    return longitude + (distance_meters * m) / math.cos(latitude * (math.pi / 180))


def get_geo_location_box(longitude, latitude, distance_meters):
    """Calculate the box sides for a geolocation (longitude, latitude) adding a distance (distance_meters).
    Returns a GeoLocationBox instance"""
    geo_location_box = GeoLocationBox(
        add_meters_to_latitude(latitude, (distance_meters * (-1))),
        add_meters_to_longitude(longitude, latitude, distance_meters),
        add_meters_to_latitude(latitude, distance_meters),
        add_meters_to_longitude(longitude, latitude, (distance_meters * (-1)))
    )
    print('GeoLocationBox: left {} top {} right {} bottom {}'.format(
        geo_location_box.left,
        geo_location_box.top,
        geo_location_box.right,
        geo_location_box.bottom))
    return geo_location_box
