import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import tkinter as tk
from tkinter import ttk

file_path = "crime.csv"
data = pd.read_csv(file_path)

class CrimeDataAnalisis:
    def __init__(self, file_path):
        self.data = pd.read_csv(file_path)

    def load_and_display_info(self):
        info_result = self.data.info()
        describe_result = self.data.describe()
        return info_result, describe_result
    
    def filter_light_crimes(self):
        light_crimes = self.data.drop(columns=['Robbery', 'Burglary', 'CarTheft'])
        print(light_crimes.describe())

    def filter_felony_crimes(self):
        felony_crimes = self.data.drop(columns=['Murder', 'Rape', 'Assault'])
        print(felony_crimes.describe())

    def the_worst_year(self):
        self.data['TotalCrime'] = self.data[['Murder', 'Rape', 'Robbery', 'Assault', 'Burglary', 'CarTheft']].eq('Yes').sum(axis=1)
        worst_year = self.data.loc[self.data['TotalCrime'].idxmax()]
        print(f"Year with the highest crime rates:\n{worst_year}\n")
        print(f"Full statistics for the worst year:\n{self.data[self.data['Year'] == worst_year['Year']].describe()}")

    def the_best_year(self):
        self.data['TotalCrime'] = self.data[['Murder', 'Rape', 'Robbery', 'Assault', 'Burglary', 'CarTheft']].eq('Yes').sum(axis=1)
        best_year = self.data.loc[self.data['TotalCrime'].idxmin()]
        print(f"Year with the lowest crime rates:\n{best_year}\n")
        print(f"Full statistics for the best year:\n{self.data[self.data['Year'] == best_year['Year']].describe()}")

    def plot_car_theft(self):
        plt.figure(figsize=(10, 6))
        plt.plot(self.data['Year'], self.data['CarTheft'], marker='o', linestyle='-')
        plt.title('Car Theft Over the Years')
        plt.xlabel('Year')
        plt.ylabel('Number of Car Thefts')
        plt.grid(True)
        plt.show()
        
    def plot_murders(self):
        plt.figure(figsize=(10, 6))
        plt.plot(self.data['Year'], self.data['Murder'], marker='o', linestyle='-')
        plt.title('Murder Over the Years')
        plt.xlabel('Year')
        plt.ylabel('Number of murders')
        plt.grid(True)
        plt.show()

class CrimeDataApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Crime Data Analysis")
        self.file_path = 'crime.csv'
        self.crime_analysis = CrimeDataAnalisis(self.file_path)
        self.create_menu()

    def create_menu(self):
        menu_frame = ttk.Frame(self.root)
        menu_frame.grid(row=0, column=0, padx=10, pady=10)
        ttk.Label(menu_frame, text="Crime Data Analysis", font=('Helvetica', 16, 'bold')).grid(row=0, column=0, columnspan=2, pady=10)
        ttk.Button(menu_frame, text="Load and Display Info", command=self.crime_analysis.load_and_display_info).grid(row=1, column=0, pady=5, sticky='ew')
        ttk.Button(menu_frame, text="Filter Light Crimes", command=self.crime_analysis.filter_light_crimes).grid(row=2, column=0, pady=5, sticky='ew')
        ttk.Button(menu_frame, text="Filter Felony Crimes", command=self.crime_analysis.filter_felony_crimes).grid(row=3, column=0, pady=5, sticky='ew')
        ttk.Button(menu_frame, text="The Worst Year", command=self.crime_analysis.the_worst_year).grid(row=4, column=0, pady=5, sticky='ew')
        ttk.Button(menu_frame, text="The Best Year", command=self.crime_analysis.the_best_year).grid(row=5, column=0, pady=5, sticky='ew')
        ttk.Button(menu_frame, text="Plot Car Theft", command=self.crime_analysis.plot_car_theft).grid(row=6, column=0, pady=5, sticky='ew')
        ttk.Button(menu_frame, text="Plot Murders", command=self.crime_analysis.plot_murders).grid(row=7, column=0, pady=5, sticky='ew')
        ttk.Button(menu_frame, text="Exit", command=self.root.destroy).grid(row=8, column=0, pady=10, sticky='ew')

if __name__ == "__main__":
    root = tk.Tk()
    app = CrimeDataApp(root)
    root.mainloop()