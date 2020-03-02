import Point

TIME_STEP = 1000 * 60

def analyze(points) :
    
    if(len(points) == 1) :
        return points[0].get_value()
    
    totalValue = 0

    for i in range(1, len(points)):
        prevIndex = i - 1
        prevPoint = points[prevIndex]
        currentPoint = points[i]
        
        totalValue += calculate_value(prevPoint, currentPoint)
        
    return totalValue

def calculate_value(prevPoint, currentPoint) :
    prevTime = prevPoint.get_time()
    currentTime =  currentPoint.get_time()

    timeDiff = (currentTime - prevTime)/ TIME_STEP
    print("timeDiff = ", timeDiff)
    
    value = currentPoint.get_value() * timeDiff
    
    return value