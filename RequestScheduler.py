import PollutionParser
import threading
import Data
import time

SCAN_DELAY = 60 # TODO: change to 3600 seconds

class RequestScheduler(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)


    def run(self):
        while True:
            points = Data.get_points()    
            new_points = PollutionParser.get_points()

            print(time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime()) + ": saving points")
            
            if points is None: Data.save_points(new_points)
            else: Data.save_points(points + new_points)
            
            time.sleep(SCAN_DELAY) 
        