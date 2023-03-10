from MPU9250.Registers import ADDRESS, REGISTER
from smbus2 import SMBus
import time


class MPU9250:
    _bus = None
    _chipId = 0x71
    _gyroOffset = (0,0,0)

    def __init__(self, busNumber, deviceAddress=ADDRESS.GYRO_ADDRESS):
        self._busNumber = busNumber
        self._deviceAddress = deviceAddress

    def init(self):
        if self._bus:
            self.close()
        self._bus = SMBus(self._busNumber)
        realChipId = self._bus.read_byte_data(self._deviceAddress, REGISTER.WHO_AM_I)
        if self._chipId != realChipId:
            raise Exception("Not correct chip id")
        self._bus.write_byte_data(self._deviceAddress, REGISTER.PWR_MGMT_1, 0x00)
        self._bus.write_byte_data(self._deviceAddress, REGISTER.SMPLRT_DIV, 0x07)
        self._bus.write_byte_data(self._deviceAddress, REGISTER.CONFIG, 0x06)
        self._bus.write_byte_data(self._deviceAddress, REGISTER.GYRO_CONFIG, 0x10)
        self._bus.write_byte_data(self._deviceAddress, REGISTER.GYRO_CONFIG, 0x10)
        time.sleep(1) #let the sensor be alone with itself
        self._gyroOffset = self.__initGyroOffset()

    def readAccel(self):
        x = self._bus.read_word_data(self._deviceAddress, REGISTER.ACCEL_XOUT_H)
        y = self._bus.read_word_data(self._deviceAddress, REGISTER.ACCEL_YOUT_H)
        z = self._bus.read_word_data(self._deviceAddress, REGISTER.ACCEL_ZOUT_H)
        return (x,y,z)
    
    def getChipId(self):
        return self._bus.read_byte_data(self._deviceAddress, REGISTER.WHO_AM_I)
    
    def readGyro(self):
        x = self._bus.read_word_data(self._deviceAddress, REGISTER.GYRO_XOUT_H)
        y = self._bus.read_word_data(self._deviceAddress, REGISTER.GYRO_YOUT_H)
        z = self._bus.read_word_data(self._deviceAddress, REGISTER.GYRO_ZOUT_H)
        return (x,y,z)
    
    #TODO digit filter

    def close(self):
        if self._bus:
            self._bus.close()

    def __initGyroOffset(self):
        count = 32
        x = 0
        y = 0
        z = 0
        for number in range(count):
            #TODO digit filter
            data = self.readGyro()
            x += data[0]
            y += data[1]
            z += data[2]
        return (x / count, y / count, z / count)
