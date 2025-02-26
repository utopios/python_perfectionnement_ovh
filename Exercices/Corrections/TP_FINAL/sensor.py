from threading import Thread
from datetime import datetime
import random
import socket
import time
import json

class Sensor(Thread):
    def __init__(self, sensor_id, location, host='localhost', port=5000):
        super().__init__()
        self.sensor_id = sensor_id
        self.location = location
        self.host = host
        self.port = port
        self.running = True

    def run(self, **options):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((self.host, self.port))
            while self.running:
                data = {
                    "id": self.sensor_id,
                    "location": self.location,
                    "timestamp": datetime.now().isoformat(),
                    "temperature": options.get("temperature"),
                    "humidity": options.get("humidity")
                }
                s.sendall(json.dumps(data).encode('utf-8'))
                time.sleep(2)

    def stop(self):
        self.running = False
