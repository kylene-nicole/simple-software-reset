# Power Reset Control for Jetson Nano

This project provides a simple GPIO-based power reset control for devices connected to the Jetson Nano. The script toggles the power on a specific GPIO pin to reset a connected device.

## Prerequisites

Before running the script, ensure the following:

1. **Jetson.GPIO Library**: This library provides access to the Jetson Nano's GPIO pins.
2. **Python 3**: The script runs on Python 3.

### Step 1: Install Required Libraries

Run the following commands to install the required libraries:

```bash
sudo apt-get update
sudo apt-get install python3-pip
pip3 install Jetson.GPIO
```

### Step 2: Wiring the Device

- **Pin 6**: Connect to Ground (GND).
- **Pin 12 (GPIO18)**: Connect the device’s power input wire here. This pin will be toggled to simulate a reset.

### Step 3: Running the Script

Once your wiring is done, you can run the script using Python 3:

```bash
python3 pull_nrst.py
```

### Step 4: Usage

The script continuously powers the device and provides an option to reset it by toggling the GPIO pin:

1. The device is powered ON when the script starts.
2. To trigger a reset, type `r` and press Enter.
3. The device power will be cut off for 1 second and then turned back ON.

### Code Overview

- **GPIO Setup**: The script initializes GPIO pin 18 (Pin 12 on the board) as an output pin to control the device power.
- **Reset Function**: The `reset_device()` function sets the pin to LOW, turning off the power momentarily, then sets it back to HIGH to power the device back on.

### Step 5: Cleanup

If you want to stop the program, press `CTRL+C`. The script will automatically clean up the GPIO setup to prevent issues on the next run.
