from threading import Lock, Semaphore
import sqlite3
from concurrent.futures import ThreadPoolExecutor
import socket
import json

class SensorServer:
    def __init__(self, host='localhost', port=5000):
        self.host = host
        self.port = port
        self.lock = Lock()
        self.max_worker = 3
        self.semaphore = Semaphore(5)
        self.db_conn = sqlite3.connect('sensors.db', check_same_thread=False)
        self.create_table()

    def create_table(self):
        cursor = self.db_conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS sensor_data (
                id TEXT,
                timestamp TEXT,
                location TEXT,
                temperature REAL,
                humidity REAL
            )
        ''')
        self.db_conn.commit()
    
    def handle_client(self, conn):
        with conn:
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                sensor_data = json.loads(data.decode('utf-8'))
                self.save_data(sensor_data)

    def save_data(self, data):
        with self.lock:
            cursor = self.db_conn.cursor()
            cursor.execute('''
                INSERT INTO sensor_data (id, timestamp, location, temperature, humidity)
                VALUES (?, ?, ?, ?, ?)
            ''', (data['id'], data['timestamp'], data['location'], data['temperature'], data['humidity']))
            self.db_conn.commit()

    def start_server(self):
        with ThreadPoolExecutor(max_workers=self.max_worker) as executor:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
                server.bind((self.host, self.port))
                server.listen()
                while True:
                    conn, _ = server.accept()
                    self.semaphore.acquire
                    executor.submit(self.handle_client, conn)
                    