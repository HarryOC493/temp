import serial
import time

# Replace 'YOUR_SERIAL_PORT' with the actual serial port of your Arduino (e.g., '/dev/ttyUSB0' or 'COM3')
ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
time.sleep(20)
print("Created serial connection")

# Function to send a request for sensor data to the Arduino
def request_sensor_data():
    ser.write(b'R')  # Encode the string 'R' to bytes

# Main loop to continuously request and read sensor data
try:
    # Open the serial connection only once
    if not ser.is_open:
        ser.open()

        # Add a 20-second delay for Arduino initialization
        time.sleep(20)
        print("Should have initialized")

    while True:
        print("Requesting data")
        request_sensor_data()

        # Read and print all data received from Arduino
        while True:
            data = ser.readline().decode().strip()
            if not data:
                break  # Break the loop if there's no more data
            print("Received:", data)

        # Add a delay to control the data update rate (in seconds)
        time.sleep(1)  # Adjust the sleep duration as needed

except KeyboardInterrupt:
    print("Exiting...")
    ser.close()  # Close the serial connection when exiting
