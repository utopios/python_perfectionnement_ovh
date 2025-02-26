import sqlite3
import xml.etree.ElementTree as ET

from PyQt6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QComboBox, QTextEdit
from PyQt6.QtCore import QTimer

def export_to_xml():
    conn = sqlite3.connect('sensors.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM sensor_data")
    rows = cursor.fetchall()

    root = ET.Element("Sensors")
    for row in rows:
        sensor = ET.SubElement(root, "Sensor")
        ET.SubElement(sensor, "ID").text = row[0]
        ET.SubElement(sensor, "Timestamp").text = row[1]
        ET.SubElement(sensor, "Location").text = row[2]
        ET.SubElement(sensor, "Temperature").text = str(row[3])
        ET.SubElement(sensor, "Humidity").text = str(row[4])

    tree = ET.ElementTree(root)
    tree.write("sensor_data.xml")
    conn.close()


class SensorMonitor(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
        
    def init_ui(self):
        self.setWindowTitle("Surveillance des Capteurs")
        self.layout = QVBoxLayout()

        self.combo = QComboBox()
        self.refresh_sensor_list()
        self.layout.addWidget(self.combo)

        self.data_display = QTextEdit()
        self.data_display.setReadOnly(True)
        self.layout.addWidget(self.data_display)

        self.export_button = QPushButton("Exporter les données en XML")
        self.export_button.clicked.connect(export_to_xml)
        self.layout.addWidget(self.export_button)

        self.refresh_button = QPushButton("Afficher les données du capteur")
        self.refresh_button.clicked.connect(self.display_sensor_data)
        self.layout.addWidget(self.refresh_button)

        self.setLayout(self.layout)
        self.timer = QTimer()
        self.timer.timeout.connect(self.refresh_sensor_list)
        self.timer.start(5000)

    def refresh_sensor_list(self):
        conn = sqlite3.connect('sensors.db')
        cursor = conn.cursor()
        cursor.execute("SELECT DISTINCT id FROM sensor_data")
        sensors = [row[0] for row in cursor.fetchall()]
        conn.close()
        self.combo.clear()
        self.combo.addItems(sensors)

    def display_sensor_data(self):
        sensor_id = self.combo.currentText()
        conn = sqlite3.connect('sensors.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM sensor_data WHERE id = ? ORDER BY timestamp DESC LIMIT 10", (sensor_id,))
        rows = cursor.fetchall()
        conn.close()

        self.data_display.clear()
        for row in rows:
            self.data_display.append(f"ID: {row[0]} | Date: {row[1]} | Lieu: {row[2]} | Temp: {row[3]}°C | Hum: {row[4]}%")