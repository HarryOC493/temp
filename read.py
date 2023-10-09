import serial
import re
import math

# Define the Arduino's serial port (change this to your port)
arduino_port = "/dev/ttyACM0"  # Linux example, may vary on Windows or macOS

# Initialize serial communication with the Arduino
ser = serial.Serial(arduino_port, baudrate=9600, timeout=1)

try:
    while True:
        # Read the incoming data
        line = ser.readline().decode('utf-8').strip()  # Decode bytes to string and remove whitespace

        # Check if the line contains relevant data
        if "Linear Acceleration" in line:
            # Extract numeric values from the line
            numeric_values = [float(num) for num in re.findall(r'-?\d+\.\d+', line)]
            
            if len(numeric_values) == 3:
                linear_acceleration = numeric_values
                print("Linear Acceleration (m/s^2): X:", linear_acceleration[0], "Y:", linear_acceleration[1], "Z:", linear_acceleration[2])

        elif "Angular Velocity" in line:
            # Extract numeric values from the line
            numeric_values = [float(num) for num in re.findall(r'-?\d+\.\d+', line)]
            
            if len(numeric_values) == 3:
                angular_velocity_deg = numeric_values
                angular_velocity_rad = [round(math.radians(deg), 3) for deg in angular_velocity_deg]
                print("Angular Velocity (rad/s): X:", angular_velocity_rad[0], "Y:", angular_velocity_rad[1], "Z:", angular_velocity_rad[2])

except KeyboardInterrupt:
    print("Keyboard interrupt detected. Exiting...")

finally:
    # Close the serial connection
    ser.close()
