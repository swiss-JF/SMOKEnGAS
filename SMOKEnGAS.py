#!/usr/bin/env python3
import csv
import time
from datetime import datetime
from pms5003 import PMS5003, ReadTimeoutError
import logging
import gas

logging.basicConfig(
    format='%(asctime)s.%(msecs)03d %(levelname)-8s %(message)s',
    level=logging.INFO,
    datefmt='%Y-%m-%d %H:%M:%S')


pms5003 = PMS5003()
time.sleep(1.0)

try:
    while True:
        try:
            with open('pms5003.csv', 'a', newline='') as csvfile:
                writer = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
                readings = pms5003.read()  # PMS5003Data instance
                dt = datetime.now()
				readings1 = pms5003.read()
				readings2 = gas.read_all() #gas data instance
				writer.writerow([dt.isoformat()] + list(readings1.data[:-2] + [readings2.oxidising, readings2.reducing, readings2.nh3, readings2.adc])
        except ReadTimeoutError:
            pms5003 = PMS5003()
except KeyboardInterrupt:
    pass