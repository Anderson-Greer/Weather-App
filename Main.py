# Created by Anderson Greer in August of 2019
# This program creates a display that gives the weather for any location

# API for this project: https://openweathermap.org/forecast5

import tkinter as tk
from tkinter import font
import random
import requests

randNum = random.randint(0, 3) # Random integer for the photo rotation
height = 600
width = 700
API_key = '6a304d3bfb52578d9e363f6465d30576'


def formatResponse(weather):
    try:
        name = weather['name']
        description = weather['weather'][0]['description']
        temp = weather['main']['temp']
        finalStr = 'City: %s \nConditions: %s \n temperature (F): %s' % (name, description, temp)

    except:
        finalStr = 'There was a problem \nlocating your city.'

    return finalStr

 # api.openweathermap.org/data/2.5/forecast?q={city name},{country code}
def findWeather(city):
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {'APPID': API_key, 'q': city, 'units': 'Imperial'}
    response = requests.get(url, params = params)
    weather = response.json()

    infoLabel['text'] = formatResponse(weather)



root = tk.Tk()

canvas = tk.Canvas(root, height = height, width = width)
canvas.pack()

if randNum == 0: # Switch statement that changes the photo when the app is launched
    backgroundImage = tk.PhotoImage(file = "weathersmall.png")
elif randNum == 1:
    backgroundImage = tk.PhotoImage(file="weatherPhoto2.png")
elif randNum == 2:
    backgroundImage = tk.PhotoImage(file="weatherPhoto3.png")
elif randNum == 3:
    backgroundImage = tk.PhotoImage(file="weatherPhoto4.png")

label = tk.Label(root, image = backgroundImage) # Creates the background
label.place(relx = 0, rely = 0, relwidth = 1, relheight = 1)

upperFrame = tk.Frame(root, bg = '#80c1ff')
upperFrame.place(relx = 0.1, rely = 0.1, relwidth = 0.8, relheight = 0.1)  # Creates the frame for the search items

searchEntry = tk.Entry(upperFrame)
searchEntry.place(relx = 0.0125, rely = 0.1, relwidth = 0.65, relheight = 0.8)  # Creates the search box

searchButton = tk.Button(upperFrame, text = 'Find Weather', command = lambda: findWeather(searchEntry.get()))  # Creates the search button
searchButton.place(relx = 0.7, rely = 0.1, relwidth = 0.2875, relheight = 0.8)

lowerFrame = tk.Frame(root, bg = '#80c1ff')
lowerFrame.place(relx = 0.1, rely = 0.35, relwidth = 0.8, relheight = 0.5)

infoLabel = tk.Label(lowerFrame, font = ('Courier', 30))
infoLabel.place(relx = 0.02, rely = 0.05, relwidth = 0.96, relheight = 0.9)

root.mainloop()




