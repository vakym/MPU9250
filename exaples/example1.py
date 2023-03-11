import os
import sys
from argparse import ArgumentParser
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from MPU9250.MPU9250 import MPU9250


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("-b", "--bus", help="I2C bus number", type=int)
    parser.add_argument("-a", "--address", help="Device address on I2C bus", type=lambda x: hex(int(x,0)))
    args = parser.parse_args()
    sensor = MPU9250(args.bus, args.address)
    sensor.init()
    print(sensor.getChipId())
    print(sensor.readAccel())
    sensor.close()