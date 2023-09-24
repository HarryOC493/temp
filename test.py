import serial
import time

# Replace 'YOUR_SERIAL_PORT' with the actual serial port of your Arduino (e.g., '/dev/ttyUSB0' or 'COM3')
ser = serial.Serial('dev/TTYACM0', 115200, timeout=1)

# Function to send a request for sensor data to the Arduino
def request_sensor_data():
    ser.write(b'R')

# Function to read and parse sensor data from the Arduino
def read_sensor_data():
    data = ser.readline().decode().strip()
    sensor_values = [float(val) for val in data.split('\t')]
    return sensor_values

# Main loop to continuously request and read sensor data
try:
    while True:
        request_sensor_data()
        sensor_values = read_sensor_data()
        
        # Store sensor values in a list (sensor_values)
        # You can access individual sensor values like sensor_values[0], sensor_values[1], etc.
        
        # Print the sensor values for demonstration
        print("Sensor Values:", sensor_values)

        # Add a delay to control the data update rate (in seconds)
        time.sleep(1)  # Adjust the sleep duration as needed

except KeyboardInterrupt:
    print("Exiting...")
    ser.close()
