import http.server
import PollutionParser
import PollutionAnalyzer
from RequestScheduler import RequestScheduler
import json
from json import JSONDecoder
from Point import get_user_point_from_json

PORT_NUMBER = 8081


# This class will handles any incoming request from
# the browser 
class myHandler(http.server.BaseHTTPRequestHandler):

    # Handler for the GET requests
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        # Send the html message
        self.wfile.write("Hello World !".encode('utf-8'))
        return

    # Handler for the POST requests
    def do_POST(self):
        value = 'null'
        self.send_response(200)
        if self.rfile:
            content_len = int(self.headers['Content-Length'])
            print(content_len)
            post_body_json = self.rfile.read(content_len)
            # value = PollutionParser.get_value(post_body_json.decode("utf-8"))
            json_array = json.loads(post_body_json.decode("utf-8"))
            points = []
            for item in json_array:
                point = JSONDecoder(object_hook = get_user_point_from_json).decode(json.dumps(item))
                points.append(point)
            
            calculated_points = []
            for i in range(0, len(points)):
                point = PollutionParser.get_recent_point(points[i][0], points[i][1], points[i][2])
                calculated_points.append(point)
                
            
            
            value = PollutionAnalyzer.analyze(calculated_points)
            print(post_body_json)
            print(value)

        self.send_header('Content-type', 'text/html')
        self.end_headers()
        # Send the html message
        self.wfile.write(bytes(str(value), "utf-8"))
        return


try:
    # Create a web server and define the handler to manage the
    # incoming request
    # value = PollutionParser.get_value("55.811801,37.71249")
    # print(value)

    scheduler = RequestScheduler()
    scheduler.start()
    server = http.server.HTTPServer(('', PORT_NUMBER), myHandler)
    print("Started httpserver on port ", PORT_NUMBER)

    # Wait forever for incoming htto requests
    server.serve_forever()
    
    

except KeyboardInterrupt:
    print('^C received, shutting down the web server')
    server.socket.close()
