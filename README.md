# Keylogger

This is a simple keylogger implemented in Python that records keystrokes and saves them to a uniquely named log file. Each time you run the keylogger, it creates a new log file with a timestamp in its name, ensuring that previous logs are not overwritten.

## Features

- Logs every key pressed on the keyboard.
- Creates a new log file for each session with a timestamp.
- Stops logging when the `ESC` key is pressed, printing the filename of the saved log.

## Requirements

- Python 3.x
- `pynput` library

## Installation

1. **Clone the repository:**

         git clone https://github.com/Anjalicy/PRODIGY_CS_04.git
         cd keylogger
   
2.Install the required package:

        pip install pynput
## Usage

 1.Run the keylogger script:

     python keylogger.py

 2.The keylogger will start running, logging all keystrokes to a new file.

 3.To stop the keylogger and save the log, press the ESC key. The script will print the name of the saved log file.
 
 ## Ethical Considerations

  Important: This keylogger is intended for educational purposes only. Always obtain explicit permission before monitoring or logging keystrokes on any       system. Unauthorized use of keyloggers is illegal and unethical.
  
## License

This project is licensed under the MIT License. See the LICENSE file for details.
