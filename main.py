import requests
from tkinter import *

api_key = 'ENTER APİ KEY'
#https://openweathermap.org/ sitesine üye olarak kendi "api key" anahtaraınızı almanız gerekmektedir.
def sehir_ismi_get():
    try:
        global sıcaklık
        sehir_ismi = (şehir_entry.get())

        url = f'http://api.openweathermap.org/data/2.5/weather?q={sehir_ismi}&appid={api_key}&lang=tr&units=metric'

        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            temp = data['main']['temp']
            desc = data['weather'][0]['description']
        else:
            print('Error fetching weather data')

        şehir_entry.delete(0,"end")

        text_box.insert('end', (f"{sehir_ismi}'da sıcaklık: {temp} C, {desc}\n"))
        text_box.config(font=("Ariel", 9, "normal"))

    except:
        print("Error!")

def silme():
    text_box.delete(1.0, "end")


window = Tk()
window.title("Hava Durumu Uygulaması")
window.minsize(width=300, height=300)
window.config(padx=20, pady=20)

icon = PhotoImage(file="icon.png.png")
icon_ = Label(image=icon)
icon_.pack()

hava_durumu_giriş = Label(text="Şehir İsmi Giriniz:", font=("Ariel", 12, "bold"))
hava_durumu_giriş.pack()
şehir_entry = Entry(width=25)
şehir_entry.pack()

getir = Button(text="Getir", command=sehir_ismi_get)
getir.config(font=("Ariel", 9, "bold"))
getir.pack()

temizle = Button(text="Temizle", command=silme)
temizle.config(font=("Ariel", 9, "bold"))
temizle.pack()

text_box = Text(height=6,width=27)
text_box.pack(expand=True)


window.mainloop()