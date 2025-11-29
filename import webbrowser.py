#a very non complicated code, create a new file in vscode or any ide of your choice and run it, change the elements in 'search_items',
#if you want to terminate, then in the terminal press 'ctrl+c'


import webbrowser
import time
import os


search_items = [
    "Tesla Model S", #car models, for examples
    "BMW X5",
    "Audi A4",
    "Mercedes GLC",
    "Toyota Supra",
    "Ford Mustang",
    "Honda Civic Type R",
    "Porsche 911",
    "Nissan GTR",
    "Lamborghini Huracan"
]


base_url = "https://www.google.com/search?q=" #search structure

for term in search_items:
    query = base_url + term.replace(" ", "+")
    webbrowser.open(query) 
    print(f"Searching for: {term}")
    time.sleep(5)  
