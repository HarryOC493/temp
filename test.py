import serial

# Define the Arduino's serial port (change this to your port)
arduino_port = "/dev/ttyACM0"  # Linux example, may vary on Windows or macOS

# Initialize serial communication with the Arduino
ser = serial.Serial(arduino_port, baudrate=9600, timeout=1)

try:
    while True:
        # Send a request to the Arduino (you can modify this command)
        ser.write(b"GetData\n")

        # Read and print the response from the Arduino
        response = ser.readline().decode().strip()
        print("Arduino Data:", response)

except KeyboardInterrupt:
    print("Keyboard interrupt detected. Exiting...")

finally:
    # Close the serial connection
    ser.close()
