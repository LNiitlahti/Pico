# This is a simple project to test the Pico board.

## Lesson 1: Embedded Programming Basics

| Task | Description | Code | Wokwi | Tested and Works |
|------|-------------|------|-------|------------------|
| 1 | Print numbers 0-9 | [task1_print_numbers.py](lesson1/task1_print_numbers.py) | [Run](https://wokwi.com/projects/443532858830928897) | ✅ |
| 2 | Name checker (Clark Kent) | [task2_name_checker.py](lesson1/task2_name_checker.py) | [Run](https://wokwi.com/projects/443533270339423233) | ✅ |
| 3 | Blink onboard LED | [task3_blink_led.py](lesson1/task3_blink_led.py) | [Run](https://wokwi.com/projects/443534177761537025) | ✅ |
| 4 | Button controlled LED | [task4_button_led.py](lesson1/task4_button_led.py) | [Run](https://wokwi.com/projects/443534652697354241) | ✅ |
| 5 | Traffic lights with buzzer | [task5_traffic_lights.py](lesson1/task5_traffic_lights.py) | [Run](https://wokwi.com/projects/443536146344851457) | ✅ |
| 6 | Reaction time game | [task6_reaction_game.py](lesson1/task6_reaction_game.py) | [Run](https://wokwi.com/projects/443536746666235905) | ✅ |
| 7 | Burglary alarm | [task7_burglary_alarm.py](lesson1/task7_burglary_alarm.py) | [Run](https://wokwi.com/projects/443537698477699073) | ✅ |
| 8 | Weather station (local) | [task8_weather_station.py](lesson1/task8_weather_station.py) | [Run](https://wokwi.com/projects/443538723743015937) | ✅ |
| 9 | Weather station (ThingSpeak) | [task9_weather_iot.py](lesson1/task9_weather_iot.py) | [Run](https://wokwi.com/projects/443538893503309825) &amp; [Example data](https://thingspeak.mathworks.com/channels/3096194) | ✅ |

## Lesson 2: Basics of backend programming

Created an Express.js server ([server.js](lesson2/server.js)) with a GET endpoint that returns JSON data with temperature, humidity, and status.

## Lesson 3: Basics of API's and databases

### IoT Pipeline: Sensor to Cloud

Created a complete IoT data pipeline ([sensor_to_thingspeak.py](lesson3/sensor_to_thingspeak.py)) that demonstrates the flow of data from sensor to cloud storage.

**Pipeline Architecture:**
```
DHT22 Sensor → Raspberry Pi Pico W → WiFi Network → Internet → ThingSpeak API → Cloud Database
```

**How the Pipeline Works:**

1. **Sensor Reading (Hardware → Software)**
   - DHT22 sensor measures temperature & humidity
   - Connected to GPIO Pin 15 on the Pico
   - MicroPython reads the data via `sensor.measure()`

2. **Data Processing**
   - Pico formats sensor values
   - Prepares data as HTTP GET request parameters

3. **Network Connection (WiFi)**
   - Pico W connects to WiFi using credentials
   - Establishes internet connectivity

4. **API Request (HTTP GET)**
   - Sends data to ThingSpeak endpoint: `http://api.thingspeak.com/update`
   - Uses JSON-formatted key-value pairs
   - Example: `?api_key=YOUR_KEY&field1=24.5&field2=60`

5. **Cloud Storage**
   - ThingSpeak receives and stores data with timestamp
   - Data viewable on dashboard with graphs and analytics

6. **Automated Loop**
   - Repeats every 20 seconds (ThingSpeak free tier minimum: 15s)

**Key Concepts:**
- **JSON**: Data format for API communication (key-value pairs)
- **API Endpoint**: Specific URL that accepts data requests
- **HTTP Methods**: Using GET to send sensor data
- **Pipeline**: Automated data flow from source to destination

## Lesson 4: Basics of frontend programming

Created an interactive IoT dashboard ([dashboard.html](lesson4/dashboard.html)) that visualizes sensor data from ThingSpeak in real-time.

**Features:**
- Real-time data fetching from ThingSpeak API
- Interactive Chart.js graphs (temperature & humidity over time)
- Auto-refresh functionality (30-second intervals)
- Discord webhook integration for notifications
  - Sends current sensor readings to Discord
  - Includes chart visualization as image attachment
  - Professional embedded message format
- Professional military-tech styling (dark theme with olive/gold accents)
- Responsive design with live activity logging