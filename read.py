import serial
import time

# Replace 'YOUR_SERIAL_PORT' with the actual serial port of your Arduino (e.g., '/dev/ttyUSB0' or 'COM3')
ser = serial.Serial('/dev/ttyACM0', 115200)

# Function to send a request for sensor data to the Arduino
def request_sensor_data():
    ser.write(b'R')

# Main loop to continuously request and read data from the Arduino
try:
    while True:
        request_sensor_data()

        # Read and print all output from the Arduino
        while ser.in_waiting:
            line = ser.readline().decode().strip()
            print(line)

        # Add a delay to control the data update rate (in seconds)
        time.sleep(1)  # Adjust the sleep duration as needed

except KeyboardInterrupt:
    print("Exiting...")
    ser.close()
