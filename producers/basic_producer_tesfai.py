"""
basic_producer_tesfai.py

Generate unique streaming buzz messages with custom content.
"""

#####################################
# Import Modules
#####################################

# Import packages from Python Standard Library
import os
import random
import time

# Import external packages (must be installed in .venv first)
from dotenv import load_dotenv

# Import functions from local modules
from utils.utils_logger import logger

#####################################
# Load Environment Variables
#####################################

# Load environment variables from .env
load_dotenv()

#####################################
# Define Getter Functions for .env Variables
#####################################

# Function to fetch the message interval from environment or default value
def get_message_interval() -> int:
    """
    Fetch message interval from environment or use default value.
    """
    return_value: str = os.getenv("MESSAGE_INTERVAL_SECONDS", 3)
    interval: int = int(return_value)
    logger.info(f"Messages will be sent every {interval} seconds.")
    return interval


#####################################
# Define global variables
#####################################

# Define some lists for generating buzz messages
# Custom message content for the producer
EMOTIONS = ["joyful", "mysterious", "adventurous", "curious", "playful", "optimistic", "melancholy", "confident"]
VERBS = ["discovered", "tried", "created", "read", "watched", "explored", "experienced", "invented"]
TOPICS = ["a documentary", "a recipe", "a coding challenge", "a hike", "a poem", "a podcast", "a conversation", "an art piece"]
LOCATIONS = ["in the park", "on a mountain", "at home", "in the city", "during a road trip", "at a cafe", "on a beach"]

#####################################
# Define a function to generate unique buzz messages
#####################################

def generate_messages():
    """
    Generate a stream of unique buzz messages using a generator.

    The generator will continuously yield one unique buzz message at a time,
    mixing emotions, verbs, topics, and locations.
    """
    while True:
        emotion = random.choice(EMOTIONS)
        verb = random.choice(VERBS)
        topic = random.choice(TOPICS)
        location = random.choice(LOCATIONS)
        # Combine the components into a dynamic message
        yield f"I {verb} {topic} {location}. It made me feel {emotion}!"

#####################################
# Define main() function to run this producer.
#####################################

def main() -> None:
    """
    Main entry point for this producer.

    It generates and logs messages every few seconds based on the environment interval.
    """
    logger.info("START producer...")
    logger.info("Hit CTRL c (or CMD c) to close.")
    
    # Get the message interval from the environment
    interval_secs: int = get_message_interval()

    for message in generate_messages():
        logger.info(message)
        # Pause execution for the specified number of seconds
        time.sleep(interval_secs)

    logger.info("NOTE: See the `logs` folder to learn more.")
    logger.info("END producer.....")


#####################################
# Conditional Execution
#####################################

# If this file is the one being executed, call the main() function
if __name__ == "__main__":
    main()
    