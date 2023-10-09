import serial

# Define the Arduino's serial port (change this to your port)
arduino_port = "/dev/ttyACM0"  # Linux example, may vary on Windows or macOS

# Initialize serial communication with the Arduino
ser = serial.Serial(arduino_port, baudrate=9600, timeout=1)

linear_acceleration = [[0.0, 0.0, 0.0]]  # Initial values
angular_velocity = [[0.0, 0.0, 0.0]]  # Initial values

try:
    while True:
        # Read the incoming data
        line = ser.readline().decode('utf-8').strip()  # Decode bytes to string and remove whitespace

        # Check if the line contains relevant data
        if "Linear Acceleration" in line:
            # Extract linear acceleration values
            values = line.split('\t')
            linear_values = [float(val.split(': ')[1]) for val in values[1:4]]
            linear_acceleration[0] = linear_values

        elif "Angular Velocity" in line:
            # Extract angular velocity values
            values = line.split('\t')
            angular_values = [float(val.split(': ')[1]) for val in values[1:4]]
            angular_velocity[0] = angular_values

except KeyboardInterrupt:
    print("Keyboard interrupt detected. Exiting...")

finally:
    # Close the serial connection
    ser.close()

# Print the collected data
print("Current Linear Acceleration:")
print(linear_acceleration[0])

print("Current Angular Velocity:")
print(angular_velocity[0])
