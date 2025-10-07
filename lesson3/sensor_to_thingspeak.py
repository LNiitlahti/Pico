# sensor_to_thingspeak.py - IoT Pipeline: Sensor to ThingSpeak (Lesson 3)

# This program creates a complete pipeline from sensor to cloud
# It reads temperature and humidity from a DHT22 sensor
# and sends the data to ThingSpeak cloud service

from machine import Pin # type: ignore (VSCODE error bypass)
import network # type: ignore (VSCODE error bypass)
import urequests # type: ignore (VSCODE error bypass)
import time
import dht # type: ignore (VSCODE error bypass)

# Import WiFi and API credentials from secrets file
try:
    from secrets import WIFI_SSID, WIFI_PASSWORD, THINGSPEAK_WRITE_API_KEY
except ImportError:
    print("ERROR: secrets.py not found!")
    print("Please copy secrets_template.py to secrets.py and add your credentials")
    raise

# ThingSpeak API endpoint
THINGSPEAK_URL = "http://api.thingspeak.com/update"

# Set up DHT22 sensor on GP15
sensor = dht.DHT22(Pin(15))

# Function to connect to WiFi
def connect_wifi():
    print("Connecting to WiFi...")
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(WIFI_SSID, WIFI_PASSWORD)

    # Wait for connection
    max_wait = 10
    while max_wait > 0:
        if wlan.status() < 0 or wlan.status() >= 3:
            break
        max_wait -= 1
        print("Waiting for connection...")
        time.sleep(1)

    # Check if connected
    if wlan.status() != 3:
        print("Network connection failed!")
        return False
    else:
        print("Connected to WiFi!")
        status = wlan.ifconfig()
        print(f"IP address: {status[0]}")
        return True

# Function to read sensor data
def read_sensor():
    try:
        sensor.measure()
        temperature = sensor.temperature()
        humidity = sensor.humidity()

        print("=" * 40)
        print("Sensor Readings:")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print("=" * 40)

        return temperature, humidity

    except Exception as e:
        print(f"Error reading sensor: {e}")
        return None, None

# Function to send data to ThingSpeak
def send_to_thingspeak(temperature, humidity):
    try:
        # Build the API request URL
        url = f"{THINGSPEAK_URL}?api_key={THINGSPEAK_WRITE_API_KEY}"
        url += f"&field1={temperature}&field2={humidity}"

        # Send HTTP GET request
        response = urequests.get(url)

        if response.status_code == 200:
            print(f"✓ Data sent successfully! Entry number: {response.text}")
        else:
            print(f"✗ Failed to send data. Status code: {response.status_code}")

        response.close()

    except Exception as e:
        print(f"Error sending to ThingSpeak: {e}")

# Main program
print("=" * 50)
print("LESSON 3: IoT Pipeline - Sensor to ThingSpeak")
print("=" * 50)
print()

# Step 1: Connect to WiFi
if not connect_wifi():
    print("Cannot continue without WiFi connection")
    print("Please check your WiFi settings in secrets.py")
else:
    print()
    print("Pipeline active: Sensor → WiFi → ThingSpeak")
    print("Sending data every 20 seconds...")
    print()

    # Wait for sensor to stabilize
    time.sleep(2)

    # Main loop - complete pipeline
    while True:
        # Read sensor data
        temp, hum = read_sensor()

        # Send to ThingSpeak cloud if data is valid
        if temp is not None and hum is not None:
            send_to_thingspeak(temp, hum)

        print()
        print("Waiting 20 seconds for next reading...")
        print()

        # Wait 20 seconds (ThingSpeak free tier minimum is 15s)
        time.sleep(20)
