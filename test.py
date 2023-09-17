import serial

# Define the serial port and baud rate
ser = serial.Serial('/dev/ttyACM0', 115200)  # Update with the correct port name

def request_data():
    # Send a request to the Arduino to request data
    ser.write(b'R')

def receive_data():
    # Read data from the Arduino until a newline character is received
    data = ser.readline().decode().strip()
    return data

def parse_sensor_data(data):
    # Split the received data by commas and convert to float values
    sensor_values = [float(value) for value in data.split(',')]
    return sensor_values

def main():
    try:
        while True:
            request_data()  # Send a request for data
            sensor_data = receive_data()  # Receive sensor data from Arduino
            if sensor_data.startswith('Data:'):
                sensor_data = sensor_data[5:]  # Remove the "Data:" prefix
                sensor_values = parse_sensor_data(sensor_data)
                # Print or process the sensor values as needed
                print("Received Sensor Values:", sensor_values)
    except KeyboardInterrupt:
        print("Script terminated.")

if __name__ == "__main__":
    main()
