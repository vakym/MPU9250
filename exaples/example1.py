import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from MPU9250.MPU9250 import MPU9250


if __name__ == "__main__":
    sensor = MPU9250(1)
    sensor.init()
    print(sensor.getChipId())
    print(sensor.readAccel())
    sensor.close()