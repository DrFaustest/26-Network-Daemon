# Network Device Identifier Program

## Description
This program is designed to scan a network, identify devices by their IP and MAC addresses, and retrieve the manufacturer information for each device. It performs a network scan, logs various events, and interacts with an external API to gather manufacturer details.

## Features
- **Network Scanning:** Leverages the 'arp' command to detect active network devices.
- **Manufacturer Identification:** Fetches device manufacturer information using the MAC address via an external API.
- **Logging System:** Includes error logs, runtime logs, and JSON data logs for comprehensive tracking.
- **Data Storage:** Stores device details (IP and MAC addresses, manufacturer) in a CSV file.

## Requirements
- Python 3.x
- External libraries: `requests`

## Installation
Clone the repository:
```bash
git clone https://github.com/DrFaustest/26-Network-Daemon
```
Install necessary libraries:
```bash
pip install requests
```

## Usage
Run the program with:
```bash
python main.py
```
After execution:
- Check `storage.csv` for the list of detected devices.
- Review log files for errors and runtime information.

## Logs
- `errorLog.txt`: Contains error logs with timestamps.
- `runLog.txt`: Logs runtime events.
- `jsonLog.txt`: Stores JSON data received from the API.

## Contributing
Contributions to improve the program are welcome. Please follow the standard process:
1. Fork the repository.
2. Create your feature branch (`git checkout -b feature/YourFeature`).
3. Commit your changes (`git commit -am 'Add some feature'`).
4. Push to the branch (`git push origin feature/YourFeature`).
5. Open a pull request.

## License
This project is licensed under the [MIT License](LICENSE.txt).

## Author
Scott Faust

## Acknowledgments
- Thanks to all contributors who have helped to improve this program.
