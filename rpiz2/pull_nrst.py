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
POWER_PIN = 18  # GPIO18 corresponds to Pin 12 on Raspberry Pi

def setup_gpio():
    """Set up GPIO pins for power control on Raspberry Pi"""
    logging.info("Setting up GPIO pins.")
    GPIO.setmode(GPIO.BCM)  # Use the BCM pin numbering
    GPIO.setup(POWER_PIN, GPIO.OUT, initial=GPIO.HIGH)  # Start with power ON (HIGH)
    logging.info("Power pin initialized, starting with power ON.")

def reset_device():
    """Reset the connected device by cutting power momentarily."""
    try:
        logging.info("Resetting device by cutting power.")
        GPIO.output(POWER_PIN, GPIO.LOW)  # Cut power (set pin LOW)
        time.sleep(1)  # Wait for 1 second (adjust time if needed)
        GPIO.output(POWER_PIN, GPIO.HIGH)  # Power back ON
        logging.info("Device power restored after reset.")
        check_pin_state()
    except Exception as e:
        logging.error(f"Failed to reset device: {e}")

def check_pin_state():
    """Check the actual state of the GPIO pin."""
    try:
        pin_state = GPIO.input(POWER_PIN)
        if pin_state == GPIO.HIGH:
            logging.info("Power pin is currently HIGH (power ON).")
        else:
            logging.warning("Power pin is LOW (power OFF).")
    except Exception as e:
        logging.error(f"Error reading power pin state: {e}")

def main_loop():
    """Main loop to keep device running and manage resets."""
    try:
        logging.info("Entering main loop. Device should be powered ON.")
        while True:
            # Placeholder for field work
            time.sleep(10)  # Simulate doing other tasks or waiting for reset trigger
            # Reset logic: Triggered by user input for simplicity, adjust based on field logic
            user_input = input("Enter 'r' to reset the device: ")
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
