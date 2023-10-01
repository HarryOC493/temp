import smbus
import time

# Define constants
I2C_BUS = 0  # Use bus 1 for I2C communication on the Jetson Nano
MPU6050_ADDRESS = 0x68  # MPU6050 I2C address

# MPU6050 register addresses
MPU6050_REGISTER_ACCEL_XOUT_H = 0x3B
MPU6050_REGISTER_PWR_MGMT_1 = 0x6B

# Initialize I2C bus
i2c = smbus.SMBus(I2C_BUS)

# Function to read 16-bit signed integer (two's complement) from MPU6050
def read_i2c_word(register):
    high_byte = i2c.read_byte_data(MPU6050_ADDRESS, register)
    low_byte = i2c.read_byte_data(MPU6050_ADDRESS, register + 1)
    value = (high_byte << 8) | low_byte
    if value >= 0x8000:
        return -((65535 - value) + 1)
    else:
        return value

# Configure MPU6050
i2c.write_byte_data(MPU6050_ADDRESS, MPU6050_REGISTER_PWR_MGMT_1, 0)

try:
    while True:
        # Read accelerometer and gyroscope data
        accel_x = read_i2c_word(MPU6050_REGISTER_ACCEL_XOUT_H)
        accel_y = read_i2c_word(MPU6050_REGISTER_ACCEL_XOUT_H + 2)
        accel_z = read_i2c_word(MPU6050_REGISTER_ACCEL_XOUT_H + 4)
        gyro_x = read_i2c_word(MPU6050_REGISTER_ACCEL_XOUT_H + 8)
        gyro_y = read_i2c_word(MPU6050_REGISTER_ACCEL_XOUT_H + 10)
        gyro_z = read_i2c_word(MPU6050_REGISTER_ACCEL_XOUT_H + 12)

        # Print sensor values
        print(f"Accelerometer (X, Y, Z): {accel_x}, {accel_y}, {accel_z}")
        print(f"Gyroscope (X, Y, Z): {gyro_x}, {gyro_y}, {gyro_z}")

        # Delay for some time (e.g., 1 second)
        time.sleep(1)

except KeyboardInterrupt:
    print("Measurement stopped by the user.")
