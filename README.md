# SIT210-Task5.1PGUI
 S306 SIT210 Task 5.1P, python GUI to control LEDs.

## Description
A simple GUI with radio buttons to cotrol a set of LEDs connected to the GPIO of a Raspberry Pi 5.

Whenever a radio button selection is changed, the corresponding LED will turn turned on, and the rest will be turned off.
Additionally, there is an exit button added so the if the GUI is modified for full screen use, there is a proper way to exit.

## How it Works
The code works by creating an LED object for each connected LED, and then controlling the state of each LED based on the selected radio button.

Two of the LEDs are tied to the ground rail, and will be lit by a `HIGH` signal on the GPIO. The third LED is a common anode RGB LED, so the common pin is tied to 3v3, and each colour is lit by a `LOW` signal on the GPIO.
```python
...
gpiozero.LED(4),                     # LED on with a HIGH signal
gpiozero.LED(17, active_high=False), # LED on with a LOW signal
...
```

Each radio button is linked to the same `selected` variable, so only one will be on at a time. A for loop has been used to minify the code for creating the buttons with a different value on selection. Finally, when the radio button selection is changed the `update` function runs and turns all LEDs off except for the currently selected one.
```
buttons = [tk.Radiobutton(window, variable=selected, value=i, command=update) for i in range(0, 6)]

# Effectivly creates:
buttons = [tk.Radiobutton(window, variable=selected, value=0, command=update),
           tk.Radiobutton(window, variable=selected, value=1, command=update),
           tk.Radiobutton(window, variable=selected, value=2, command=update),
           tk.Radiobutton(window, variable=selected, value=3, command=update),
           tk.Radiobutton(window, variable=selected, value=4, command=update),
           tk.Radiobutton(window, variable=selected, value=5, command=update)]
```

## Usage
Requires the following libraries:
* gpiozero
* tkinter