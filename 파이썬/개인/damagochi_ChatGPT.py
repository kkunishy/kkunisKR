import tkinter as tk
from tkinter import messagebox
import random

class Tamagotchi:
    def __init__(self, name):
        self.name = name
        self.hunger = 0
        self.happiness = 0

    def feed(self):
        self.hunger -= 10
        if self.hunger < 0:
            self.hunger = 0
        self.update_status()

    def play(self):
        self.happiness += 10
        if self.happiness > 100:
            self.happiness = 100
        self.update_status()

    def update_status(self):
        status_text.set(f"Name: {self.name}\nHunger: {self.hunger}\nHappiness: {self.happiness}")

    def check_status(self):
        if self.hunger >= 100:
            messagebox.showinfo("Game Over", "Your Tamagotchi is too hungry. Game Over!")
            window.destroy()
        elif self.happiness <= 0:
            messagebox.showinfo("Game Over", "Your Tamagotchi is too unhappy. Game Over!")
            window.destroy()

    def decrease_status(self):
        self.hunger += random.randint(5, 15)
        self.happiness -= random.randint(5, 15)
        self.check_status()
        self.update_status()
        window.after(5000, self.decrease_status)

# Create a new Tamagotchi instance
tamagotchi = Tamagotchi("Tammy")

# Create the main window
window = tk.Tk()
window.title("Tamagotchi")

# Create the status label
status_text = tk.StringVar()
status_label = tk.Label(window, textvariable=status_text, font=("Arial", 12))
status_label.pack(pady=10)

# Create the feed button
feed_button = tk.Button(window, text="Feed", width=10, command=tamagotchi.feed)
feed_button.pack(pady=5)

# Create the play button
play_button = tk.Button(window, text="Play", width=10, command=tamagotchi.play)
play_button.pack(pady=5)

# Start decreasing status after 5 seconds
window.after(5000, tamagotchi.decrease_status)

# Run the main loop
window.mainloop()

