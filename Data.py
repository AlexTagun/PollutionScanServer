import os
from DataEncoder import DataEncoder
import json
from json import JSONDecoder

from Point import Point
from Point import get_point_from_json

def get_points():
    path = os.path.join("data.txt")
    if not os.path.exists(path):
        return None
    input_file = open ('data.txt')
    json_array = json.load(input_file)
    points = []
    for item in json_array:
        point = JSONDecoder(object_hook = get_point_from_json).decode(json.dumps(item))
        points.append(point)
    return points

def save_points(points):
    with open("data.txt", "w") as document:
        json = DataEncoder().encode(points)
        document.writelines(json)
