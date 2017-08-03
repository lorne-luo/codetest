from math import cos, asin, sqrt

DEPOT_LATITUDE = -37.816664
DEPOT_LONGITUDE = 144.963848
PI_PER_ANGLE = 0.017453292519943295  # Pi/180
DRONE_SPEED = 20.0  # km/h


class Position(object):
    latitude = None
    longitude = None

    def __init__(self, longitude, latitude):
        self.longitude = longitude
        self.latitude = latitude

    def get_distance(self, pos):
        """distance in km"""
        a = 0.5 - cos((pos.latitude - self.latitude) * PI_PER_ANGLE) / 2 + cos(self.latitude * PI_PER_ANGLE) * cos(
            pos.latitude * PI_PER_ANGLE) * (1 - cos((pos.longitude - self.longitude) * PI_PER_ANGLE)) / 2
        return 12742 * asin(sqrt(a))  # 2*R*asin...

    def get_delivery_time(self, pos):
        """delivery time in hour"""
        distance = self.get_distance(pos)
        return distance / 20.0


DEPOT = Position(DEPOT_LONGITUDE, DEPOT_LATITUDE)


