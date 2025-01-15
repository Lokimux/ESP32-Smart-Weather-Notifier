# ESP32 Telegram Bot for DHT11 Sensor

This project uses an ESP8266 microcontroller to read temperature and humidity data from a DHT11 sensor and send the data to a Telegram group using a bot.

## Features
- Connects to Wi-Fi.
- Reads temperature and humidity data from the DHT11 sensor.
- Sends data to a Telegram group as a Markdown-formatted message.

## Prerequisites
1. **Hardware**:
   - ESP32 microcontroller.
   - DHT11 temperature and humidity sensor.
   - Jumper wires.
   - Breadboard.

2. **Software**:
   - [MicroPython firmware](https://micropython.org/download/).
   - Tools to flash firmware (e.g., `esptool.py`).
   - A Telegram bot ([Create one using BotFather](https://core.telegram.org/bots#botfather)).

## Connections
| **DHT11 Pin** | **ESP32 Pin**   |
|---------------|-----------------|
| VCC           | 3.3V            |
| GND           | GND             |
| Data          | GPIO14          |

> Update the pin number in the code if a different pin is used.

## Setup Instructions
1. Flash MicroPython firmware on your ESP32.
2. Upload the required files (`main.py` and `urequests` library) to the ESP8266 using tools like `ampy` or `Thonny`.
3. Replace the placeholders in the code:
   - `your_wifi_ssid` with your Wi-Fi SSID.
   - `your_wifi_password` with your Wi-Fi password.
   - `your_bot_token` with your Telegram bot token.
   - `your_group_chat_id` with your Telegram group chat ID.

4. Run the `main.py` file on the ESP32.

## Usage
- The ESP8266 will connect to the Wi-Fi network and start sending temperature and humidity readings to the specified Telegram group every 15 seconds.

## License
This project is open-source and licensed under the MIT License.
