# task9_weather_iot.py - Weather station with ThingSpeak IoT (C) Lassi Niitlahti

# This program reads temperature and humidity from a DHT22 sensor
# It displays the readings on the serial monitor
# It sends the data to ThingSpeak cloud service every 20 seconds

from machine import Pin # type: ignore (VSCODE error bypass)
import network # type: ignore (VSCODE error bypass)
import urequests # type: ignore (VSCODE error bypass)
import time
import dht # type: ignore (VSCODE error bypass)

# Import WiFi and API credentials from secrets file
# Make sure you have created secrets.py from secrets_template.py!
try:
    from secrets import WIFI_SSID, WIFI_PASSWORD, THINGSPEAK_WRITE_API_KEY
except ImportError:
    print("ERROR: secrets.py not found!")
    print("Please copy secrets_template.py to secrets.py and add your credentials")
    raise

# ThingSpeak URL
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

# Function to send data to ThingSpeak
def send_to_thingspeak(temperature, humidity):
    try:
        # Build the URL with parameters
        url = f"{THINGSPEAK_URL}?api_key={THINGSPEAK_WRITE_API_KEY}"
        url += f"&field1={temperature}&field2={humidity}"
        
        # Send HTTP GET request
        response = urequests.get(url)
        
        if response.status_code == 200:
            print(f"Data sent to ThingSpeak successfully! Entry: {response.text}")
        else:
            print(f"Failed to send data. Status code: {response.status_code}")
        
        response.close()
        
    except Exception as e:
        print(f"Error sending to ThingSpeak: {e}")

# Function to read and display sensor data (same as task8!)
def read_weather():
    try:
        # Measure temperature and humidity
        sensor.measure()
        
        # Get the values
        temperature = sensor.temperature()
        humidity = sensor.humidity()
        
        # Display the readings
        print("=" * 30)
        print("Weather Station Readings:")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print("=" * 30)
        print()
        
        return temperature, humidity
        
    except Exception as e:
        print(f"Error reading sensor: {e}")
        return None, None

# Main program
print("===== WEATHER STATION IOT =====")
print("Connecting to network and ThingSpeak...")
print()

# Connect to WiFi first
if not connect_wifi():
    print("Cannot continue without WiFi connection")
    print("Please check your WiFi settings in secrets.py")
else:
    print()
    print("Starting weather monitoring...")
    print("Reading sensor and sending to ThingSpeak every 20 seconds")
    print()
    
    # Wait a moment for sensor to stabilize
    time.sleep(2)
    
    # Main loop - read sensor and send to cloud
    while True:
        # Read weather data (same function as task8!)
        temp, hum = read_weather()
        
        # Send to ThingSpeak if we got valid readings
        if temp is not None and hum is not None:
            send_to_thingspeak(temp, hum)
        
        # Wait 20 seconds before next reading
        # ThingSpeak free account allows updates every 15 seconds minimum
        time.sleep(20)