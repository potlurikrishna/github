import requests

BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'

def get_weather_data(city, api_key, units='metric'):
    try:
        params = {
            'q': city,
            'appid': api_key,
            'units': units
        }
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()  # Raise an HTTPError for bad responses
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None

def display_weather(data, units):
    if data:
        main = data['main']
        wind = data['wind']
        weather = data['weather'][0]
        temp_unit = 'C' if units == 'metric' else 'F'
        print(f"\nCity: {data['name']}")
        print(f"Temperature: {main['temp']}°{temp_unit}")
        print(f"Humidity: {main['humidity']}%")
        print(f"Wind Speed: {wind['speed']} m/s")
        print(f"Weather: {weather['description'].capitalize()}\n")
    else:
        print("No data to display.")

def main():
    api_key = input("Enter your OpenWeatherMap API key: ")
    city = input("Enter the city name: ")
    unit_choice = input("Choose the unit for temperature (C for Celsius, F for Fahrenheit): ").strip().upper()
    units = 'metric' if unit_choice == 'C' else 'imperial'

    weather_data = get_weather_data(city, api_key, units)
    if weather_data and weather_data.get('cod') == 200:
        display_weather(weather_data, units)
    else:
        print("Invalid city name or unable to fetch weather data.")

if __name__ == "__main__":
    main()
