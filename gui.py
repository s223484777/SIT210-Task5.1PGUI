#!/usr/bin/env python

import gpiozero
import tkinter as tk

# Setup LEDs
leds = [gpiozero.LED(2),                     # GPIO  2, Blue LED anode
        gpiozero.LED(3),                     # GPIO  3, Dual LED green anode
        gpiozero.LED(4),                     # GPIO  4, Dual LED red anode
        gpiozero.LED(17, active_high=False), # GPIO 17, RGB LED blue cathode
        gpiozero.LED(27, active_high=False), # GPIO 27, RGB LED green cathode
        gpiozero.LED(22, active_high=False)] # GPIO 22, RGB LED red cathode
for led in leds: led.off()

# Setup Tkinter window
window = tk.Tk()
window.title("LED Controller")

# Update the LED states to match the current selection
selected = tk.IntVar()
def update():
  for i in range(0, len(leds)):
    if i == selected.get():
      leds[i].on()
    else:
      leds[i].off()

# Setup labels and buttons
labels = [tk.Label(window, text="Single LED Blue", width=24),
          tk.Label(window, text="Dual LED Green", width=24),
          tk.Label(window, text="Dual LED Red", width=24),
          tk.Label(window, text="RGB LED Blue", width=24),
          tk.Label(window, text="RGB LED Green", width=24),
          tk.Label(window, text="RGB LED Red", width=24)]
for i in range(len(labels)): labels[i].grid(row=i, column=0)

buttons = [tk.Radiobutton(window, variable=selected, value=i, command=update) for i in range(0, 6)]
for i in range(len(buttons)):
  buttons[i].grid(row=i, column=1)

buttons.append(tk.Button(window, text="Exit", command=window.destroy))
buttons[-1].grid(row=len(buttons) - 1, column=1)

# Update the initial status and run the main loop
update()
window.mainloop()