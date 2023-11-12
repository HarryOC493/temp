import serial
import matplotlib.pyplot as plt
import numpy as np

# Setup the serial connection (Change the COM port as necessary)
ser = serial.Serial('/dev/tty.usbmodem14101', 9600)  # Update port

# Setup the matplotlib plot
plt.ion()  # Enable interactive mode
fig, ax = plt.subplots()
line1, = ax.plot([], [], 'ro-')  # Initialize a line plot

# Function to update the plot
def update_line(thigh, knee, ankle):
    # Define the segments (assuming simple 2D representation)
    thigh_length = 1
    knee_length = 1
    ankle_length = 0.5

    # Convert angles to radians
    thigh_rad = np.radians(thigh)
    knee_rad = np.radians(knee)
    ankle_rad = np.radians(ankle)

    # Calculate the joint positions
    x = [0, thigh_length * np.sin(thigh_rad), 
         thigh_length * np.sin(thigh_rad) + knee_length * np.sin(thigh_rad + knee_rad),
         thigh_length * np.sin(thigh_rad) + knee_length * np.sin(thigh_rad + knee_rad) + ankle_length * np.sin(thigh_rad + knee_rad + ankle_rad)]
    y = [0, thigh_length * np.cos(thigh_rad), 
         thigh_length * np.cos(thigh_rad) + knee_length * np.cos(thigh_rad + knee_rad),
         thigh_length * np.cos(thigh_rad) + knee_length * np.cos(thigh_rad + knee_rad) + ankle_length * np.cos(thigh_rad + knee_rad + ankle_rad)]

    line1.set_xdata(x)
    line1.set_ydata(y)
    ax.relim()
    ax.autoscale_view()
    fig.canvas.draw()
    fig.canvas.flush_events()

# Main loop
while True:
    if ser.in_waiting:
        line = ser.readline().decode('utf-8').rstrip()
        angles = [float(val) for val in line.split(',')]
        if len(angles) == 3:
            update_line(angles[0], angles[1], angles[2])
