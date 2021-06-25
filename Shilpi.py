import requests
#import os
from datetime import datetime
import sys #to write or push output in a text file

api_key = 'd541c87d8c16d4d904419f17a11c4d53'
place = input("Enter the name of the place: ")

complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+place+"&appid="+api_key
api_link = requests.get(complete_api_link)
api_data = api_link.json()

#creating variables
temp_C = ((api_data['main']['temp']) - 273.15)
temp_F = (temp_C*(9/5))+32
desc = api_data['weather'][0]['description']
hum = api_data['main']['humidity']
wind_speed = api_data['wind']['speed']
date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

sys.stdout = open("Shilpi_Weather.txt","w")


print("-----------------------------------------------------------------------")
print("Weather Statistics for - {} || {}".format(place.upper(), date_time))
print("-----------------------------------------------------------------------")

print("Current Temperature in degree Celcius is {:.1f} deg C".format(temp_C))
print("Current Temperature in degree Fahrenheit is {:.1f} deg F".format(temp_F))
print("Current Weather Description: ",desc.title())
print("Current Humidity: ",hum,"%")
print("Current Wind Speed: ",wind_speed,"kmph")

sys.stdout.close()
