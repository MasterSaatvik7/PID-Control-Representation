# PID Controller for Drone Height Adjustment

## Overview

This project implements a **PID controller** to regulate the height of a drone. The PID (Proportional-Integral-Derivative) controller adjusts the drone's height over time to reach a desired target height, minimizing error through feedback control.

## PID Controller Explanation

The PID control law is given by the equation:

$$u(t) = K_p e(t) + K_i \int e(t) dt + K_d \frac{d}{dt} e(t)$$

where:

- $$u(t)$$ is the control output (adjustment applied to height)
- $$e(t) = \text{target height} - \text{current height}$$ is the error at time $$t$$
- $$K_p$$ is the **Proportional gain** (reacts to present error)
- $$K_i$$ is the **Integral gain** (reacts to accumulated past errors)
- $$K_d$$ is the **Derivative gain** (reacts to rate of error change)

## Features

- Accepts user-defined PID parameters $$K_p, K_i, K_d$$
- Allows customization of target height, initial height, time steps, and time interval
- Computes PID control output iteratively
- Displays a tabulated report of PID calculations
- Plots a **smoothed height trajectory** using cubic spline interpolation

## Installation

Ensure you have Python and the required libraries installed:

```bash
pip install numpy scipy pandas matplotlib
```

## Usage

Run the script and input the required values when prompted:

```bash
python pid.py
```

The script prompts for:

- **PID parameters**: $$K_p, K_i, K_d$$
- **Target height**
- **Initial height**
- **Total time steps**
- **Time interval**

## Simulation Process

1. Initialize the system with user-defined parameters.
2. Iteratively compute:
   - Error: $$e(t) = \text{target height} - \text{current height}$$
   - Integral error: $$\sum e(t)$$
   - Derivative error: $$\frac{e(t-1) - e(t)}{\Delta t}$$
   - PID control output: $$u(t)$$
   - Updated height: $$\text{current height} + u(t)$$
3. Store and display results in tabular format.
4. Plot the height trajectory.

## Example Output Table

| t   | e(t) | Cumulative Error | Rate of Change of Error | u(t) | Current Height (after PID) |
| --- | ---- | ---------------- | ----------------------- | ---- | -------------------------- |
| 0   | 5.0  | 5.0              | 0.0                     | 1.1  | 46.1                       |
| 1   | 3.9  | 8.9              | -1.1                    | 1.2  | 47.3                       |
| ... | ...  | ...              | ...                     | ...  | ...                        |

## Visualization

The script generates a graph depicting the drone's height over time:

- **Blue curve**: Smoothed height trajectory using cubic spline interpolation.
- **Red dashed line**: Target height.

## Applications

This PID control implementation is widely applicable in:

- **Drone altitude control**
- **Autonomous vehicle navigation**
- **Industrial process automation**

## Author

[Saatvik Sumanta - VIT Chennai]

## License

This project is open-source and available under the MIT License.

