import smbus
from Registers import REGISTER, ADDRESS
import time


class MPU9250:
    _bus = None
    _chip_id = 0x71

    def __init__(self, bus_number):
        self._bus_number = bus_number

    def init(self):
        if self._bus:
            self.close()
        self._bus = smbus.SMBus(self._bus_number)
        real_chip_id = self._bus.read_byte_data(self._device_address, REGISTER.WHO_AM_I)
        if self._chip_id != real_chip_id:
            raise Exception("Not correct chip id")
        self._bus.write_byte_data(ADDRESS.GYRO_ADDRESS, REGISTER.PWR_MGMT_1, 0x00)
        self._bus.write_byte_data(ADDRESS.GYRO_ADDRESS, REGISTER.SMPLRT_DIV, 0x07)
        self._bus.write_byte_data(ADDRESS.GYRO_ADDRESS, REGISTER.CONFIG, 0x06)
        self._bus.write_byte_data(ADDRESS.GYRO_ADDRESS, REGISTER.GYRO_CONFIG, 0x10)
        self._bus.write_byte_data(ADDRESS.GYRO_ADDRESS, REGISTER.GYRO_CONFIG, 0x10)
        time.sleep(1) #let the sensor be alone with itself

    def readAccel(self):
        x = self._bus.read_word_data(ADDRESS.ACCEL_ADDRESS, REGISTER.ACCEL_XOUT_H)
        y = self._bus.read_word_data(ADDRESS.ACCEL_ADDRESS, REGISTER.ACCEL_YOUT_H)
        z = self._bus.read_word_data(ADDRESS.ACCEL_ADDRESS, REGISTER.ACCEL_ZOUT_H)
        return (x,y,z)
                

    def close(self):
        if self._bus:
            self._bus.close()