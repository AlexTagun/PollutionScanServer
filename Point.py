
class Point:
    def __init__(self, x, y, value, time):
        self.x = x
        self.y = y
        self.value = value
        self.time = time

def get_point_from_json(json_object):
        return Point(json_object['x'], json_object['y'], json_object['value'], json_object['time'])