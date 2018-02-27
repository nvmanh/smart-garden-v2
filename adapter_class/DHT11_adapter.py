import logging
import time
import datetime
from datetime import datetime
from config import HOSTNAME
import Adafruit_DHT
import RPi.GPIO as GPIO

MODULE_NAME = 'DHT11_Adapter'

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
    datefmt='%m-%d %H:%M',
    filename='./../log/adapter_log.log'
)

class DHT11_adapter:
    sensor = 11
    SENSOR_TYPE = 'DHT11'

    def __init__(self, gpio, sensor_id):
        logging.info(MODULE_NAME + ": constructor start")
        self.sensor_id = sensor_id
        self.gpio = gpio

    def read(self):
        return Adafruit_DHT.read_retry(self.sensor, self.gpio)

    def readJSON(self):
        self.status = GPIO.input(self.gpio)
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        d_dht11 = {'hostname': HOSTNAME,
                 'type': self.SENSOR_TYPE,
                 'sensorid': self.sensor_id,
                 'state': self.status,
                 'datetime': str(timestamp)}
        return d_dht11
