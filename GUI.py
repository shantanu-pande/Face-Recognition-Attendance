import cv2
import tkinter as tk
from PIL import ImageTk, Image

window = tk.Tk()
window.title("OpenCV Application")
window.geometry("300x200")
def update_camera():
    ret, frame = cap.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    image = Image.fromarray(frame)
    image = ImageTk.PhotoImage(image)
    label.configure(image=image)
    label.image = image
    label.after(10, update_camera)

def button1_click():
    # Code for button1 click action
    print("Button 1 clicked")

def button2_click():
    # Code for button2 click action
    print("Button 2 clicked")

cap = cv2.VideoCapture(0)

label = tk.Label(window, padx=100, pady=100)
label.pack(padx=10, pady=10)

button_frame = tk.Frame(window)
button_frame.pack()

button1 = tk.Button(button_frame, text="Check In", command=button1_click)
button1.pack(side="left", padx=100, pady=10)

button2 = tk.Button(button_frame, text="Check Out", command=button2_click)
button2.pack(side="left", padx=100, pady=10)

update_camera()

window.mainloop()
