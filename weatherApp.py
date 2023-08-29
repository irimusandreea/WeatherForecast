import requests
from tkinter import *
import math

city_name = "city,country"

api_key = "api_key"

def get_weather(api_key, city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

    response = requests.get(url).json()

    temp = response['main']['temp']
    temp = math.floor(temp - 273.15) #converting to C

    feels_like = response['main']['feels_like']
    feels_like = math.floor(feels_like - 273.15)  # converting to C

    humidity = response['main']['humidity']

    description = response['weather'][0]['description']


    return {
        'temp': temp,
        'feels_like': feels_like,
        'humidity': humidity,
        'description' : description
    }

weather = get_weather(api_key, city_name)

app = Tk()
app.geometry("300x300")
app.configure(bg="pink")
app.title(f'{city_name[:-3]} Weather Forecast')

def display_city_name(city):
    city_label = Label(app, text=f"{city_name[:-3]}", background="pink")
    city_label.config(font=("Cheri", 28))
    city_label.pack(side='top')

def display_winfo(weather):
    temp = Label(app, text=f"Temperature: {weather['temp']}\N{DEGREE SIGN}C", background="pink")
    feels_like = Label(app, text=f"Feels like: {weather['feels_like']}\N{DEGREE SIGN}C", background="pink")
    humidity = Label(app, text=f"Humidity: {weather['humidity']}%", background="pink")
    description = Label(app, text=f"Description: {weather['description']}", background="pink")

    temp.config(font=("Cheri", 22))
    feels_like.config(font=("Cheri", 16))
    humidity.config(font=("Cheri", 16))
    description.config(font=("Cheri", 16))

    temp.pack(side='top')
    feels_like.pack(side='top')
    humidity.pack(side='top')
    description.pack(side='top')


display_city_name(city_name)
display_winfo(weather)
mainloop()
