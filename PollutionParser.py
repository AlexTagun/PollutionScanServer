import urllib.request
import json
import sys
import math
from Point import Point
import time
import Data


def get_points():
    fp = urllib.request.urlopen("https://aqicn.org/map/moscow/ru/#")
    mybytes = fp.read()
    
    body = mybytes.decode("utf8")
    fp.close()
    
    a = body.index("mapInitWithData")
    
    substring = body[a + 16:]
    b = substring.index(";")
    substring = substring[:b - 1]
    
    c = substring.index("meta")
    substring = substring[:c - 3]

    data = json.loads(substring)
    
    points = []
    for point in data:
        coordinates = point["g"]
        value = point["aqi"]
        coordinates = float(coordinates[0]) , float(coordinates[1])
        timeInMilliseconds =  int(round(time.time() * 1000))
        points.append(Point(float(coordinates[0]), float(coordinates[1]), value, timeInMilliseconds))
        
    return points
    
def get_nearest_points(x, y):
    points = Data.get_points()
    
    min_dist = sys.float_info.max
    point_index = -1
    
    
    
    for i in range(0, len(points)):
        dist = math.sqrt(pow(points[i].x - x, 2) + pow(points[i].y - y, 2))
        if dist < min_dist:
            min_dist = dist
            point_index = i

    nearest_points = []
    for i in range(0, len(points)):
        if(points[i].x == points[point_index].x and points[i].y == points[point_index].y):
            nearest_points.append(points[i])
    return nearest_points

def get_recent_point(x, y, time):
    nearest_points = get_nearest_points(x, y)
    min_time = sys.float_info.max
    point_index = -1
    for i in range(0, len(nearest_points)):
        if(abs(time - nearest_points[i].time) < min_time):
            min_time = abs(time - nearest_points[i].time)
            point_index = i
    print(point_index)
    return  nearest_points[point_index]
