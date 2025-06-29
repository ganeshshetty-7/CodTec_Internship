import requests
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import pandas as pd
import sys


print("-"*5,"Next 5 Days Temperature of City","-"*5)
# User input for city
CITY = input("Enter city name: ")

#OpenWeatherMap API key
API_KEY = "8a52a56c93809fce1237919418c75c18"
URL = f"http://api.openweathermap.org/data/2.5/forecast?q={CITY}&appid={API_KEY}&units=metric"

# Fetch data
response = requests.get(URL)
if response.status_code != 200:
    print("Failed to fetch data. Check your API key or city name.")
    sys.exit()

data = response.json()
forecast_list = data['list']

# Parse data
dates = [datetime.strptime(item['dt_txt'], '%Y-%m-%d %H:%M:%S') for item in forecast_list]
temperatures = [item['main']['temp'] for item in forecast_list]

df = pd.DataFrame({'DateTime': dates, 'Temperature (°C)': temperatures})

# Plot 
sns.set(style="darkgrid")
plt.figure(figsize=(12, 6))
sns.lineplot(data=df, x="DateTime", y="Temperature (°C)", marker="o")
plt.title(f"Temperature Forecast for {CITY}", fontsize=16)
plt.xlabel("Date and Time")
plt.ylabel("Temperature (°C)")
plt.xticks(rotation=45)
plt.tight_layout()

#To Save the chart
plt.savefig(f"{CITY}_forecast.png", dpi=300)
plt.show()
