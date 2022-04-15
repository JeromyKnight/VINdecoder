from tkinter import *
import requests
import json

root = Tk()
root.title('VIN Decoder v1.1')

root.geometry("390x200")

e = Entry(root, width=35, bg="light gray")
e.grid(row=1, column=1, padx=20, pady=5)
e.insert(0,"1D4GP25E36B749644")

def clear(): # clear results from previous vin search
    myLabel = Label(root, text='                                                                 ')
    myLabel.grid(row=2, column=1)
    myLabel1 = Label(root, text='                                                                       ')
    myLabel1.grid(row=3, column=1)
    myLabel2 = Label(root, text='                                                                       ')
    myLabel2.grid(row=4, column=1)
    myLabel3 = Label(root, text='                                                                       ')
    myLabel3.grid(row=5, column=1)        
    myLabel4 = Label(root, text='                                                                       ')
    myLabel4.grid(row=6, column=1) 

def myClick(): # perform vin search and output results
    vin = e.get()
    url = (f'https://vpic.nhtsa.dot.gov/api/vehicles/DecodeVinValues/{vin}?format=json')

    r = requests.get(url)
    for question in r.json()['Results']:
        Yr = question["ModelYear"]
        Make = question["Make"]
        Model = question["Model"]
        Displacement = question["DisplacementL"]
        Cylinders = question["EngineCylinders"]

    myLabel = Label(root, text=f'Year: {Yr}') 
    myLabel.grid(row=2, column=1)

    myLabel1 = Label(root, text=f'Make: {Make}')
    myLabel1.grid(row=3, column=1)

    myLabel2 = Label(root, text=f'Model: {Model}')
    myLabel2.grid(row=4, column=1)

    myLabel3 = Label(root, text=f'Displacement: {Displacement}')
    myLabel3.grid(row=5, column=1)

    myLabel4 = Label(root, text=f'# Cyl: {Cylinders}')
    myLabel4.grid(row=6, column=1)
    
myLabel1 = Label(root, text="Enter a VIN to test the decoder")
myLabel1.grid(row=0, column=1, padx=25, pady=5)

myButton = Button(root, text='Search', padx=25, bg="light gray", command=myClick)
myButton.grid(row=1, column= 2, padx=5, pady=5)

clearbutton = Button(root, text='Clear', padx=30, bg="light gray", command=clear)
clearbutton.grid(row=2, padx=20, column=2)

root.mainloop()
