import serial

# Define the Arduino's serial port (change this to your port)
arduino_port = "/dev/ttyACM0"  # Linux example, may vary on Windows or macOS

# Initialize serial communication with the Arduino
ser = serial.Serial(arduino_port, baudrate=9600, timeout=1)

try:
    while True:
        # Read the incoming data
        line = ser.readline().decode().strip()

        # Check if the data starts with the specified header
        if line.startswith("SENSOR_DATA:"):
            # Process the sensor data (remove the header and convert to int)
            sensor_data = int(line[len("SENSOR_DATA:"):])
            print("Received Sensor Data:", sensor_data)

        # Add other code here as needed...

except KeyboardInterrupt:
    print("Keyboard interrupt detected. Exiting...")

finally:
    # Close the serial connection
    ser.close()
