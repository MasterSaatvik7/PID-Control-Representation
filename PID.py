import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline
import pandas as pd

def get_valid_input(prompt, input_type=float):
    while True:
        try:
            value = input_type(input(prompt))
            return value
        except ValueError:
            print(f"Invalid input. Please enter a valid {input_type.__name__}.")

# Parameters
Kp = get_valid_input('Enter Kp Value: ', float) #2       # Proportional gain
Ki = get_valid_input('Enter Ki Value: ', float) #0.1     # Integral gain
Kd = get_valid_input('Enter Kd Value: ', float) #0.1    # Derivative gain
target_height = get_valid_input('Enter target height: ', float) #50  # Target height in meters

# Simulation parameters
initial_height = get_valid_input('Enter initial height: ', float) #45  # Initial height in meters
time_steps = get_valid_input('Enter Total Timesteps: ', int) #21      # Total time steps to simulate
timestep = get_valid_input('Enter Time interval: ', float) #1         # Time interval between steps

# Variables
height = [initial_height]  # List to store heights
error = []                 # List to store errors
integral_error = 0         # Cumulative error
previous_error = target_height - initial_height  # Initial error
pid_output = []            # List to store PID output
rate_of_change_error = []  # List to store derivative of error

# Simulation loop
for t in range(time_steps):
    # Calculate error
    current_error = target_height - height[-1]
    error.append(current_error)
    
    # Update integral and derivative of error
    integral_error += current_error
    derivative_error = (previous_error - current_error) / timestep  # Fixed formula
    rate_of_change_error.append(derivative_error)
    
    # Calculate PID output
    u = (Kp * current_error) + (Ki * integral_error) + (Kd * derivative_error)
    pid_output.append(u)
    
    # Update height
    new_height = height[-1] + u
    height.append(new_height)
    
    # Update previous error
    previous_error = current_error

# Time steps for plotting and table
time = list(range(time_steps + 1))  # +1 to include the initial height at t=0

# Create a DataFrame for the table
data = {
    "t": list(range(time_steps)),
    "e(t)": error,
    "Cumulative Error": [sum(error[:i + 1]) for i in range(len(error))],
    "Rate of Change of Error": rate_of_change_error,
    "u(t)": pid_output,
    "Current Height (after PID)": height[1:]  # Skip the initial height
}

df = pd.DataFrame(data)

# Print the table
print("PID Controller Calculations:")
print(df.to_string(index=False))

# Create smooth curve using interpolation
time_smooth = np.linspace(min(time), max(time), 300)  # Generate more time points for smoothing
height_smooth = make_interp_spline(range(len(height)), height, k=3)(time_smooth)  # Cubic spline interpolation

# Plot results
plt.figure(figsize=(10, 6))
plt.plot(time_smooth, height_smooth, label="Smoothed Height", color='b')
plt.axhline(target_height, color='r', linestyle='--', label="Target Height")
plt.xlabel("Time (s)")
plt.ylabel("Height (m)")
plt.title("Drone Height Adjustment with PID Control (Smoothed)")
plt.legend()
plt.grid()
plt.show()