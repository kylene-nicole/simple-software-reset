# Button Event Trigger on Jetson Nano

This project demonstrates a simple button press event using GPIO pins on the Jetson Nano. The button press triggers an increment of a counter, but the script is designed to be easily extendable for triggering any event in the future.

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

### Step 2: Wiring the Button

For the wiring, you can connect the button to **Pin 11 (GPIO17)** and **Pin 9 (GND)** as follows:

- **Pin 9 (GND)**: Connect to one side of the push button.
- **Pin 11 (GPIO17)**: Connect the other side of the push button to GPIO17.

When the button is pressed, it will complete the circuit and pull the GPIO pin LOW.

### Step 3: Running the Script

Once your wiring is done, you can run the script using Python 3:

```bash
python3 button_counter.py
```

### Step 4: Usage

- The script will start and wait for a button press.
- Each button press will increment the counter and log the event in `button_event.log`.
- You can see real-time logs in the console, as well as the counter increment.

### Code Overview

- **GPIO Setup**: The script initializes GPIO pin 17 (Pin 11 on the board) as an input pin to detect the button press.
- **Button Event**: The `button_event()` function is triggered on each button press. Currently, it increments a counter and logs the event. In the future, you can modify this function to trigger any custom event.

### Step 5: Cleanup

If you want to stop the program, press `CTRL+C`. The script will automatically clean up the GPIO setup to prevent issues on the next run.

---

## Future Modification Notes

When you want to trigger any other event in the future, simply replace the `button_event()` function's contents. For example, you can:
- Call other functions.
- Send a network request.
- Trigger hardware components like LEDs or motors.
