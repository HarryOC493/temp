import serial

# Replace 'YOUR_SERIAL_PORT' with the actual serial port of your Arduino (e.g., '/dev/ttyUSB0' or 'COM3')
ser = serial.Serial('/dev/ttyACM0', 115200, timeout=1)

# Function to send a request for sensor data to the Arduino
def request_sensor_data():
    ser.write(b'R')

# Main loop to continuously send 'R' and print responses until a blank line is received
try:
    while True:
        request_sensor_data()
        
        # Read and print responses until a blank line is received
        while True:
            line = ser.readline().decode().strip()
            if not line:
                break
            print(line)

except KeyboardInterrupt:
    print("Exiting...")
    ser.close()
