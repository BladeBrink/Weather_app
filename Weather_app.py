import requests
from tkinter import *
from tkinter import messagebox
import json
import pycountry

def country_to_code(country_text):
    if country_text == "":
        messagebox.showerror('Error','Please enter a country for a more accurate search next time')
    else:
        try:
            country = pycountry.countries.get(name=country_text)
            return country.alpha_2
        except AttributeError:
            messagebox.showerror('Error','Can not find country {}. Showing most relevant result'.format(country_text))


def get_weather(city,country_code):
    api_key = "17c660983a0ba305885a262f5c8c364d"
    try:
        geo_coding_api = requests.get(f"http://api.openweathermap.org/geo/1.0/direct?q={city},{country_code}&limit=1&appid={api_key}")
        area_data = json.loads(geo_coding_api.content)
        lat = area_data[0]['lat']
        long = area_data[0]['lon']
        weather_api_request = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={long}&appid={api_key}")
        weather_data = json.loads(weather_api_request.content)
        city = weather_data['name']
        country = weather_data['sys']['country']
        temp_kelvin = weather_data['main']['temp']
        temp_celcius = temp_kelvin - 273.15
        temp_fer = (temp_kelvin - 273.15) * 9/5 + 32
        icon = weather_data['weather'][0]['icon']
        weather = weather_data['weather'][0]['main']
        final = (city,country,temp_celcius,temp_fer,icon,weather)
        return final
    except:
        messagebox.showerror('Error','Can not find city {}'.format(city))


def search():
    city = city_text.get()
    country_code = country_to_code(country_text.get())
    weather = get_weather(city,country_code)
    location_lbl['text'] = '{},{}'.format(weather[0],weather[1]) 
    image['bitmap'] = ('{}@2x.png'.format(weather[4]))
    temp_lbl['text'] = '{:.2f}"C,{:.2f}"F'.format(weather[2],weather[3])
    weather_lbl['text']=weather[5]




app = Tk()
app.title("Weather App")
app.geometry("300x350")

city_lbl = Label(app,text="City: ")
city_lbl.grid(column=2,row=0)

city_text = StringVar()
city_entry= Entry(app, textvariable=city_text)
city_entry.grid(row=0, column=3)

country_lbl = Label(app,text="Country: ")
country_lbl.grid(column=2,row=1)

country_text = StringVar()
country_entry = Entry(app,textvariable=country_text)
country_entry.grid(column=3,row=1)

search_btn = Button(app,text="Search Weather", width = 12, command = search)
search_btn.grid(column = 3,row=2)

location_lbl = Label(app,text='', font = ('bold',20))
location_lbl.grid(column = 3,row = 3)

image = Label(app,bitmap='')
image.grid(column = 3,row = 4)

temp_lbl = Label(app,text = '')
temp_lbl.grid(column = 3,row = 6)

weather_lbl = Label(app,text = '')
weather_lbl.grid(column = 3,row = 7)

app.mainloop()
