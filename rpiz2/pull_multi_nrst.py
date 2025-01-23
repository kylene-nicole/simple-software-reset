# multiple pull with sense c hat is not tested yet for zero 2w

import RPi.GPIO as GPIO
import time
import logging
import sys

# Logging setup
logging.basicConfig(
    filename='power_reset_control.log',
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
)
console_handler = logging.StreamHandler(sys.stdout)
console_handler.setLevel(logging.INFO)
console_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
console_handler.setFormatter(console_formatter)
logging.getLogger().addHandler(console_handler)

# Pin definitions
POWER_PINS = [17, 18, 27, 22]  # List of GPIO pins for power control
# Raspberry Pi Zero 2W:
# https://datasheets.raspberrypi.com/rpizero2/raspberry-pi-zero-2-w-reduced-schematics.pdf
# P0 = GPIO17 = Pin 11
# P1 = GPIO18 = Pin 12
# P2 = GPIO27 = Pin 13
# P3 = GPIO22 = Pin 15


def setup_gpio():
    """Set up GPIO pins for power control on Raspberry Pi"""
    logging.info("Setting up GPIO pins.")
    GPIO.setmode(GPIO.BCM)  # Use the BCM pin numbering
    for pin in POWER_PINS:
        GPIO.setup(pin, GPIO.OUT, initial=GPIO.HIGH)  # Start with power ON (HIGH)
        logging.info(f"Power pin {pin} initialized, starting with power ON.")

def reset_device():
    """Reset all connected devices by cutting power momentarily."""
    try:
        logging.info("Resetting devices by cutting power.")
        for pin in POWER_PINS:
            logging.info(f"Cutting power for pin {pin}.")
            GPIO.output(pin, GPIO.LOW)  # Cut power (set pin LOW)
        time.sleep(1)  # Wait for 1 second (adjust time if needed)
        for pin in POWER_PINS:
            GPIO.output(pin, GPIO.HIGH)  # Power back ON
            logging.info(f"Power restored for pin {pin}.")
        check_pin_states()
    except Exception as e:
        logging.error(f"Failed to reset devices: {e}")

def check_pin_states():
    """Check the actual state of all GPIO pins."""
    try:
        for pin in POWER_PINS:
            pin_state = GPIO.input(pin)
            if pin_state == GPIO.HIGH:
                logging.info(f"Power pin {pin} is currently HIGH (power ON).")
            else:
                logging.warning(f"Power pin {pin} is LOW (power OFF).")
    except Exception as e:
        logging.error(f"Error reading power pin states: {e}")

def main_loop():
    """Main loop to keep device running and manage resets."""
    try:
        logging.info("Entering main loop. Devices should be powered ON.")
        while True:
            user_input = input("Enter 'r' to reset the devices: ")
            if user_input.lower() == 'r':
                reset_device()

    except KeyboardInterrupt:
        logging.info("Program interrupted by user.")

    except Exception as e:
        logging.error(f"Unexpected error in main loop: {e}")

    finally:
        logging.info("Cleaning up GPIO settings.")
        GPIO.cleanup()
        logging.info("Program exiting cleanly.")

if __name__ == "__main__":
    setup_gpio()
    main_loop()
