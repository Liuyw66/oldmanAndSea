import logging
import time

# Configure logging
logging.basicConfig(level=logging.INFO)

def show_blood_effect(intensity=1, duration=2):
    """
    Logic to display blood effect.
    
    Parameters:
    intensity (int): The intensity of the blood effect (1-10).
    duration (int): The duration for which the effect is displayed in seconds.
    """
    try:
        # Simulate displaying the blood effect
        logging.info(f"Displaying blood effect with intensity {intensity} for {duration} seconds.")
        # Here you would integrate with the actual graphics engine to show the effect
        time.sleep(duration)  # Simulate the duration of the effect
        logging.info("Blood effect ended.")
    except Exception as e:
        logging.error(f"Error displaying blood effect: {e}")

def capture_feedback(success=True, message="Fish captured!"):
    """
    Logic for feedback when fish is captured.
    
    Parameters:
    success (bool): Indicates if the capture was successful.
    message (str): The message to display for the capture feedback.
    """
    try:
        if success:
            logging.info(f"Capture feedback shown: {message}")
            # Here you would integrate with the actual graphics engine to show the feedback
        else:
            logging.info("Capture feedback shown: Capture failed.")
    except Exception as e:
        logging.error(f"Error showing capture feedback: {e}")
