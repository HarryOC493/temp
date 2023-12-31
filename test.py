import serial

# Define the Arduino's serial port (change this to your port)
arduino_port = "/dev/ttyACM0"  # Linux example, may vary on Windows or macOS

# Initialize serial communication with the Arduino
ser = serial.Serial(arduino_port, baudrate=115200, timeout=1)

#ser = serial.Serial(
#    port="/dev/ttyTHS1",
#    baudrate=115200,
#    bytesize=serial.EIGHTBITS,
#    parity=serial.PARITY_NONE,
#    stopbits=serial.STOPBITS_ONE,
#)
try:
    while True:
        # Read the incoming data
        line = ser.readline()
        # Print all serial data received from the Arduino
        print("Arduino Data:", line)

except KeyboardInterrupt:
    print("Keyboard interrupt detected. Exiting...")

finally:
    # Close the serial connection
    ser.close()
