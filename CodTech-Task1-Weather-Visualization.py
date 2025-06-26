import requests
import matplotlib.pyplot as plt

# Function to fetch weather data from OpenWeatherMap API
def fetch_weather_data(city, api_key):
    """
    Sends a GET request to the weather API for a specific city.

    Parameters:
    city (str): Name of the city
    api_key (str): Your OpenWeatherMap API key

    Returns:
    dict: Parsed JSON weather data if successful, else None
    """
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()
    else:
        print("Failed to fetch data. Please check the city name or API key.")
        return None

# Function to visualize weather data
def visualize_weather_data(city, data):
    """
    Creates a bar chart for temperature, humidity, and wind speed.

    Parameters:
    city (str): Name of the city
    data (dict): Weather data retrieved from API
    """
    # Define labels and values to plot
    labels = ['Temperature (°C)', 'Humidity (%)', 'Wind Speed (m/s)']
    values = [
        data['main']['temp'],       # Temperature
        data['main']['humidity'],   # Humidity
        data['wind']['speed']       # Wind Speed
    ]

    # Create a bar chart
    plt.figure(figsize=(8, 5))
    bars = plt.bar(labels, values, color=['skyblue', 'lightgreen', 'salmon'])
    plt.title(f"Weather Data for {city}")
    plt.ylabel("Values")

    # Annotate each bar with its value
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + 0.1, yval + 0.5, round(yval, 2))

    # Save the chart as an image
    plt.tight_layout()
    plt.savefig("weather_dashboard.png")
    plt.show()

# Main function to run the script
if __name__ == "__main__":
    # Your actual API key
    api_key = "709a67e33a5309f69704f4975321f793"
    
    # City name can be changed if needed
    city = "Coimbatore"

    # Fetch weather data and visualize it
    data = fetch_weather_data(city, api_key)
    if data:
        visualize_weather_data(city, data)
