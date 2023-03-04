from enum import IntFlag

class REGISTER(IntFlag):
# define MPU9250 register address
    SMPLRT_DIV = 0x19  #Sample Rate Divider. Typical values:0x07(125Hz) 1KHz internal sample rate
    CONFIG = 0x1A #Low Pass Filter.Typical values:0x06(5Hz)
    GYRO_CONFIG = 0x1B #Gyro Full Scale Select. Typical values:0x10(1000dps)
    ACCEL_CONFIG = 0x1C #Accel Full Scale Select. Typical values:0x01(2g)

    ACCEL_XOUT_H = 0x3B
    ACCEL_XOUT_L = 0x3C
    ACCEL_YOUT_H = 0x3D
    ACCEL_YOUT_L = 0x3E
    ACCEL_ZOUT_H = 0x3F
    ACCEL_ZOUT_L = 0x40

    TEMP_OUT_H = 0x41
    TEMP_OUT_L = 0x42

    GYRO_XOUT_H = 0x43
    GYRO_XOUT_L = 0x44
    GYRO_YOUT_H = 0x45
    GYRO_YOUT_L = 0x46
    GYRO_ZOUT_H = 0x47
    GYRO_ZOUT_L = 0x48

    MAG_XOUT_L = 0x03
    MAG_XOUT_H = 0x04
    MAG_YOUT_L = 0x05
    MAG_YOUT_H = 0x06
    MAG_ZOUT_L = 0x07
    MAG_ZOUT_H = 0x08


    PWR_MGMT_1 = 0x6B #Power Management. Typical values:0x00(run mode)
    WHO_AM_I = 0x75 #identity of the device

class ADDRESS(IntFlag):
    GYRO_ADDRESS = 0xD0 #Gyro and Accel device address
    MAG_ADDRESS =  0x18 #compass device address
    ACCEL_ADDRESS = 0xD0 

    ADDRESS_AD0_LOW = 0xD0 #address pin low (GND), default for InvenSense evaluation board
    ADDRESS_AD0_HIGH =  0xD1 #address pin high (VCC)
    DEFAULT_ADDRESS = GYRO_ADDRESS
    WHO_AM_I_VAL = 0x73 #identity of MPU9250 is 0x71. identity of MPU9255 is 0x73.
