import serial

# Define the serial port and baud rate
ser = serial.Serial('/dev/ttyACM0', 115200)  # Update with the correct port name

def request_data():
    # Send a request to the Arduino to request data
    ser.write(b'R')

def receive_and_print_data():
    # Read data from the Arduino until a newline character is received
    data = ser.readline().decode().strip()
    print("Received Data:", data)

def main():
    try:
        while True:
            request_data()  # Send a request for data
            receive_and_print_data()  # Receive and print sensor data from Arduino
    except KeyboardInterrupt:
        print("Script terminated.")

if __name__ == "__main__":
    main()
