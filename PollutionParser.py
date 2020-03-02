import urllib.request
import json
import sys
import math
from Point import Point
import time


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
    
def get_value(coordinates_data):
    coordinates = coordinates_data.split(",")
    coordinates = float(coordinates[0]) , float(coordinates[1])
    # print(coordinates)
    
    points = get_points()
    # print(points)
    
    min_dist = sys.float_info.max
    point_index = -1
    
    for i in range(0, len(points)):
        x = points[i][0][0]
        y = points[i][0][1]
        dist = math.sqrt(pow(x - coordinates[0], 2) + pow(y - coordinates[1], 2))
        if dist < min_dist:
            min_dist = dist
            point_index = i
    return points[point_index][1]

def get_point_from_client(jsonData) :
    
    return points
