"""
Task:

1. Read the file and clean extra spaces.
2. Remove duplicates.
3. Sort devices alphabetically.
4. Print the total count of unique devices and each device on a new line.

"""
import logging
from typing import List

"""
1. logging module

Why?

In small scripts, people often just use print() to show output. But in professional code (what interviewers expect for backend/automation), we use logging because:

You can control the level of importance (INFO, WARNING, ERROR).

You can easily redirect logs to a file instead of console.

Logs include timestamps → useful in production debugging.

"""

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def dev_inventory_cleaner(input_file: str, output_file: str) -> None:
    """
    Reads a device list from a file, removes duplicates, cleans spaces,
    sorts the list alphabetically, and writes the results to an output file.
    
    Args:
        input_file (str): Path to the input file containing device names.
        output_file (str): Path to the output file where results will be written.

    Returns:
        None
    """
    try:
        with open(input_file, "r") as f:
            lines = f.readlines()
            if not lines:
                logging.warning("Input file is empty. Nothing to process.")
                return

        # Clean spaces and remove duplicates using a set
        unique_devices = {line.strip() for line in lines if line.strip()}

        # Sort devices alphabetically
        sorted_devices: List[str] = sorted(unique_devices)

        # Write cleaned results to output file
        with open(output_file, "w") as out:
            out.write("\n".join(sorted_devices))
            out.write(f"\n\nTotal Count of unique devices: {len(sorted_devices)}\n")

        # Print to console as well
        logging.info(f"Processed {len(lines)} lines from {input_file}.")
        logging.info(f"Found {len(sorted_devices)} unique devices.")
        print(f"Total unique devices: {len(sorted_devices)}")
        for device in sorted_devices:
            print(device)

    except FileNotFoundError:
        logging.error(f"Error: {input_file} not found.")
    except Exception as e:
        logging.error(f"Unexpected error: {e}")

# Example usage
if __name__ == "__main__":
    dev_inventory_cleaner("devices.txt", "ans_list.txt")
