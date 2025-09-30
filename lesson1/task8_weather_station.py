# task8_weather_station.py - Local weather station with DHT22 sensor (C) Lassi Niitlahti

# This program reads temperature and humidity from a DHT22 sensor
# It displays the readings on the serial monitor
# The readings are updated every 10 seconds

from machine import Pin # type: ignore (VSCODE error bypass)
import time
import dht # type: ignore (VSCODE error bypass)

# Set up DHT22 sensor on GP15
sensor = dht.DHT22(Pin(15))

# Function to read and display sensor data
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
print("===== WEATHER STATION =====")
print("Starting weather monitoring...")
print("Reading sensor every 10 seconds")
print()

# Wait a moment for sensor to stabilize
time.sleep(2)

# Main loop - read sensor continuously
while True:
    # Read and display weather data
    temp, hum = read_weather()
    
    # Wait 10 seconds before next reading
    # DHT22 sensor needs at least 2 seconds between readings
    time.sleep(10)