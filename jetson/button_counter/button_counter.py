import Jetson.GPIO as GPIO
import time
import logging
import sys

# Logging setup
logging.basicConfig(
    filename='button_event.log',
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
)
console_handler = logging.StreamHandler(sys.stdout)
console_handler.setLevel(logging.INFO)
console_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
console_handler.setFormatter(console_formatter)
logging.getLogger().addHandler(console_handler)

# Pin definitions
BUTTON_PIN = 17  # GPIO17 corresponds to Pin 11

# Counter
counter = 0

def setup_gpio():
    """Set up GPIO pins for the button."""
    logging.info("Setting up GPIO pins.")
    GPIO.setmode(GPIO.BCM)  # Use the BCM pin numbering
    GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # Set up as an input with pull-up resistor
    logging.info("Button pin initialized.")

def button_event(channel):
    """Event triggered when the button is pressed."""
    global counter
    counter += 1
    logging.info(f"Button pressed! Counter: {counter}")
    # In the future, you can trigger any event here
    # For example, you can call a function or send data somewhere
    # trigger_any_event()

def main_loop():
    """Main loop to detect button presses and trigger events."""
    try:
        logging.info("Waiting for button press...")
        # Detects rising edge on the button press (from low to high signal)
        GPIO.add_event_detect(BUTTON_PIN, GPIO.FALLING, callback=button_event, bouncetime=300)

        # Keep the program running
        while True:
            time.sleep(1)  # Main thread doing nothing, just waiting for button press

    except KeyboardInterrupt:
        logging.info("Program interrupted by user.")

    finally:
        logging.info("Cleaning up GPIO settings.")
        GPIO.cleanup()
        logging.info("Program exiting cleanly.")

if __name__ == "__main__":
    setup_gpio()
    main_loop()
