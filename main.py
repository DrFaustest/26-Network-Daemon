import subprocess
import re
import requests
import csv
from datetime import datetime

def log_error(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open('errorLog.txt', 'a') as file:
        file.write(f"{timestamp} - ERROR - {message}\n")

def log_run(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open('runLog.txt', 'a') as file:
        file.write(f"{timestamp} - RUN - {message}\n")

def log_json(data):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open('jsonLog.txt', 'a') as file:
        file.write(f"{timestamp} - JSON - {data}\n")

def ping_network():
    try:
        result = subprocess.run(['arp', '-a'], capture_output=True, text=True)
        output = result.stdout
        ip_mac_pairs = re.findall(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+([0-9A-Fa-f]{2}(?:[:-][0-9A-Fa-f]{2}){5})', output)
        return set(ip_mac_pairs)
    except Exception as e:
        log_error(f"ping_network: {e}")
        return set()

def get_device_manufacturer(mac_address):
    if "ff-ff-ff-ff-ff-ff" in mac_address:
        return 'Broadcast Address'

    try:
        url = f"https://api.maclookup.app/v2/macs/{mac_address}/company/name"
        response = requests.get(url)
        if response.status_code == 200:
            company_name = response.text.strip()
            log_run(f"API Call Successful: {company_name}")  # Log successful API call
            return company_name
        else:
            log_error(f"API Call Unsuccessful: {response.status_code}")
            return 'Unknown'
    except Exception as e:
        log_error(f"get_device_manufacturer: {e}")
        return 'Error'



def store_data(ip_address, mac_address, manufacturer):
    try:
        with open('storage.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([ip_address, mac_address, manufacturer])
    except Exception as e:
        log_error(f"store_data: {e}")

ip_mac_pairs = ping_network()
processed_count = 0
for ip, mac in ip_mac_pairs:
    manufacturer = get_device_manufacturer(mac)
    store_data(ip, mac, manufacturer)
    processed_count += 1

log_run(f"Processed {processed_count} IP-MAC pairs.")
