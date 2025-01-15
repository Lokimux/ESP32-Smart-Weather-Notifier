import network
import time
import urequests
from machine import Pin
import dht

# Wi-Fi credentials
WIFI_SSID = "your_wifi_ssid"  # Replace with your Wi-Fi SSID during deployment
WIFI_PASSWORD = "your_wifi_password"  # Replace with your Wi-Fi password during deployment

# Telegram bot credentials
TELEGRAM_BOT_TOKEN = "your_bot_token"  # Replace with your Telegram Bot Token during deployment
GROUP_CHAT_ID = "your_group_chat_id"  # Replace with your Telegram group chat ID during deployment

# DHT11 setup
dht_pin = Pin(14)  # Pin where the DHT11 data pin is connected
sensor = dht.DHT11(dht_pin)

# Connect to Wi-Fi
def connect_wifi(ssid, password):
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print("Connecting to Wi-Fi...")
        wlan.connect(ssid, password)
        while not wlan.isconnected():
            time.sleep(1)
    print("Connected to Wi-Fi!")
    print("Network config:", wlan.ifconfig())

# Send message to Telegram with Markdown table formatting
def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": GROUP_CHAT_ID,
        "text": message,
        "parse_mode": "MarkdownV2"
    }
    try:
        response = urequests.post(url, json=payload)
        if response.status_code == 200:
            print("Message sent to Telegram!")
        else:
            print("Failed to send message:", response.text)
        response.close()
    except Exception as e:
        print("Error sending message:", e)

# Read data from the DHT11 sensor and format as a Markdown table
def read_dht_sensor():
    try:
        sensor.measure()
        temperature = sensor.temperature()
        humidity = sensor.humidity()
        
        message = (
            "*Temperature and Humidity Readings*\n"
            "```\n"
            "-----------------------------\n"
            "| Parameter    | Value      |\n"
            "|--------------|------------|\n"
            f"| Temperature  | {temperature} °C      |\n"
            f"| Humidity     | {humidity}%        |\n"
            "-----------------------------\n"
            "```"
        )
        return message
    except Exception as e:
        print("Error reading from DHT11:", e)
        return "*Failed to read sensor data.*"

# Main function to send data periodically
def main():
    connect_wifi(WIFI_SSID, WIFI_PASSWORD)
    
    while True:
        message = read_dht_sensor()
        send_telegram_message(message)
        time.sleep(15)

# Run the main function
main()
