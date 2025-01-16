# basic_consumer_tesfai.py

# Read a log file as it is being written. 
#####################################
# Import Modules
#####################################

# Import packages from Python Standard Library
import os
import time

# Import functions from local modules
from utils.utils_logger import logger, get_log_file_path

#####################################
# Define a function to process a single message
#####################################

def process_message(log_file) -> None:
    """
    Read a log file and process each message.

    Args:
        log_file (str): The path to the log file to read.
    """
    with open(log_file, "r") as file:
        # Move to the end of the file
        file.seek(0, os.SEEK_END)
        print("Consumer is ready and waiting for a new log message...")

        # Use while True loop so the consumer keeps running forever
        while True:

            # Read the next line of the file
            line = file.readline()

            # If the line is empty, wait for a new log entry
            if not line:
                # Wait a second for a new log entry
                delay_seconds = 1
                time.sleep(delay_seconds)
                # Keep checking for new log entries
                continue

            # We got a new log entry!
            # Remove any leading/trailing white space and log the message
            message = line.strip()
            print(f"Consumed log message: {message}")

            # Categorize and respond to messages based on their content
            if "discovery" in message:
                print(f"ALERT: Discovery message detected! \n{message}")
                logger.info(f"Discovery Alert: {message}")
            elif "achievement" in message:
                print(f"ALERT: Achievement message detected! \n{message}")
                logger.info(f"Achievement Alert: {message}")
            elif "adventure" in message:
                print(f"ALERT: Adventure message detected! \n{message}")
                logger.info(f"Adventure Alert: {message}")
            else:
                print(f"INFO: Regular buzz message: {message}")
                logger.info(f"Regular Buzz: {message}")


#####################################
# Define main function for this script.
#####################################

def main() -> None:
    """Main entry point."""

    logger.info("START consumer...")

    # Get the log file path from the logger utility
    log_file_path = get_log_file_path()
    logger.info(f"Reading file located at {log_file_path}.")

    try:
        # Process the messages from the log file
        process_message(log_file_path)

    except KeyboardInterrupt:
        print("User stopped the process.")

    logger.info("END consumer.....")


#####################################
# Conditional Execution
#####################################

# If this file is the one being executed, call the main() function
if __name__ == "__main__":
    main()
