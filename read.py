import serial

# Define the Arduino's serial port (change this to your port)
arduino_port = "/dev/ttyACM0"  # Linux example, may vary on Windows or macOS

# Initialize serial communication with the Arduino
ser = serial.Serial(arduino_port, baudrate=9600, timeout=1)

linear_acceleration_data = []
angular_velocity_data = []

try:
    while True:
        # Read the incoming data
        line = ser.readline().decode('utf-8').strip()  # Decode bytes to string and remove whitespace

        # Check if the line contains relevant data
        if "Linear Acceleration" in line:
            # Extract linear acceleration values
            values = line.split('\t')
            linear_values = [float(val.split(': ')[1]) for val in values[1:4]]
            linear_acceleration_data.append(linear_values)
        
        elif "Angular Velocity" in line:
            # Extract angular velocity values
            values = line.split('\t')
            angular_values = [float(val.split(': ')[1]) for val in values[1:4]]
            angular_velocity_data.append(angular_values)

        # Print the collected data
        print("Linear Acceleration Data:")
        for data in linear_acceleration_data:
            print(data)
        
        print("Angular Velocity Data:")
        for data in angular_velocity_data:
            print(data)

except KeyboardInterrupt:
    print("Keyboard interrupt detected. Exiting...")

finally:
    # Close the serial connection
    ser.close()


