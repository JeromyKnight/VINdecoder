import customtkinter as ctk
import requests

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("345x275")
        self.title("VIN Search 2.0")
        
root = App()
#root.iconbitmap("car2.ico")

e = ctk.CTkEntry(root, 
                 width=200, 
                 fg_color="black",
                 text_color="white",
                 font=ctk.CTkFont(family="arial", size=17)
                 )

e.grid(row=1, column=0, columnspan=2, padx=20, pady=5)
e.insert(0,"zff79ala3g0217410")

def clear(): # clear results from previous vin search
    myLabel = ctk.CTkLabel(root, text='                                                                                  ')
    myLabel.grid(row=3, column=0, columnspan=2)
    myLabel1 = ctk.CTkLabel(root, text='                                                                                 ')
    myLabel1.grid(row=4, column=0, columnspan=2)
    myLabel2 = ctk.CTkLabel(root, text='                                                                                 ')
    myLabel2.grid(row=5, column=0, columnspan=2)
    myLabel3 = ctk.CTkLabel(root, text='                                                                                 ')
    myLabel3.grid(row=6, column=0, columnspan=2)        
    myLabel4 = ctk.CTkLabel(root, text='                                                                                 ')
    myLabel4.grid(row=7, column=0, columnspan=2) 

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

    myLabel = ctk.CTkLabel(root, 
                           text=f'Year: {Yr}',
                           font=ctk.CTkFont(family="arial", size=17)
                           )
    myLabel.grid(row=3, column=0, columnspan=2)

    myLabel1 = ctk.CTkLabel(root, 
                            text=f'Make: {Make}',
                            font=ctk.CTkFont(family="arial", size=17)
                           )
    myLabel1.grid(row=4, column=0, columnspan=2)

    myLabel2 = ctk.CTkLabel(root, 
                            text=f'Model: {Model}',
                            font=ctk.CTkFont(family="arial", size=17)
                           )
    myLabel2.grid(row=5, column=0, columnspan=2)

    myLabel3 = ctk.CTkLabel(root, 
                            text=f'Displacement: {Displacement}',
                            font=ctk.CTkFont(family="arial", size=17)
                           )
    myLabel3.grid(row=6, column=0, columnspan=2)

    myLabel4 = ctk.CTkLabel(root, 
                            text=f'# Cyl: {Cylinders}',
                            font=ctk.CTkFont(family="arial", size=17)
                           )
    myLabel4.grid(row=7, column=0, columnspan=2)
    
myLabel1 = ctk.CTkLabel(root, 
                        text="Enter a VIN to search NHTSA.gov",
                        font=ctk.CTkFont(family="arial", size=17)
                        )
myLabel1.grid(row=0, column=0, columnspan=2, padx=25, pady=5)

myButton = ctk.CTkButton(root, 
                         text='Search',
                         fg_color="black", 
                         command=myClick)
myButton.grid(row=2, column= 1, padx=5, pady=5)

clearbutton = ctk.CTkButton(root, 
                        text='Clear', 
                        fg_color="black", 
                        command=clear)
clearbutton.grid(row=2, padx=20, column=0)

root.mainloop()
