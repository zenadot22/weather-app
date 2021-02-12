from tkinter import*
from tkinter import messagebox

def state_weather():
    import requests, json


    weather_key = 'e36ee04de7275d14d11645a67e3a8dcb'


    url = 'https://api.openweathermap.org/data/2.5/weather'


    city_name = Ecity.get()
    params1 = {'appid':weather_key, 'q': city_name, 'units': 'Metric'}
    response = requests.get(url, params=params1)
    weather = response.json()

    if weather['cod'] != '404':
        y=weather['main']
        current_temp=y['temp']
        current_pressure=y['pressure']
        current_humid=y['humidity']
        z=weather['weather']
        weather_descript= z[0]['description']
        Etemp.insert(15, str(current_temp)+ "" +'Degrees')
        Eatm.insert(10, str(current_pressure)+ "" +'hPa')
        Ehumid.insert(15, str(current_humid)+ "" +'%')
        Edescrit.insert(10, str(weather_descript))
    else:
        messagebox.showerror('Error','Please enter a valid City'  '\n')

        Ecity.delete(0, END)

def clear1():
    Ecity.delete(0, END)
    Etemp.delete(0, END)
    Eatm.delete(0, END)
    Ehumid.delete(0,END)
    Edescrit.delete(0, END)

    Ecity.focus_set()

if __name__ == "__main__":

    root = Tk()
    root.geometry('400x200')
    root.config(bg='red')
    root.title('Weather app')

    Ecity = Entry(root, text='Enter city', width=40)
    label_city = Label(root, text='City', width=20, bg='blue', fg='white')

    Etemp = Entry(root, width=40)

    Eatm = Entry(root, width=40)
    Ehumid = Entry(root, width =40)
    Edescrit = Entry(root, width=40)
    Ecity.grid(column=1, row=0), Etemp.grid(column=1, row=1), Eatm.grid(column=1, row=4), Ehumid.grid(column=1, row=5) ,Edescrit.grid(column=1, row=6)

    label_temp = Label(root, text='Temperature', width=20, bg='blue', fg='white')
    label_atm = Label(root, text='Atmospheric pressure', width=20, bg='blue', fg='white')
    label_humid = Label(root, text='Humidity', width=20, bg='blue', fg='white')
    label_descript = Label(root, text='Description', width=20, bg='blue', fg='white')
    label_city.grid(column=0, row=0), label_temp.grid(column=0, row=1), label_atm.grid(column=0, row=4), label_humid.grid(column=0, row=5), label_descript.grid(column=0, row=6)

    check_button= Button(root, text='Check', width=10, bg='black', fg='white', command=state_weather)
    clear_button = Button(root, text=' Clear', width=10, bg='black', fg='white', command=clear1)
    check_button.grid(column=1, row=2), clear_button.grid(column=1, row=7)

    root.mainloop()

