import tkinter as tk
import cv2
from PIL import ImageTk, Image

class CameraApp:
    def __init__(self, window):
        self.window = window
        self.window.title("Attendance System")
        self.window.geometry("500x600")

        # Create a label to display the camera feed
        self.label = tk.Label(window)
        self.label.pack(padx=10, pady=10)

         # Create a label to display additional information
        self.info_label = tk.Label(window, text="Name: ", font=("Arial", 12, "bold"))
        self.info_label.pack(pady=5)
        self.info_label = tk.Label(window, text="Registration number: ")
        self.info_label.pack(pady=5)
        self.info_label = tk.Label(window, text="Division: ")
        self.info_label.pack(pady=5)
        self.info_label = tk.Label(window, text="Roll Number: ")
        self.info_label.pack(pady=5)

        # Create a frame for the buttons
        self.buttons_frame = tk.Frame(window)
        self.buttons_frame.pack(padx=10, pady=10)

        # Create the "Start" button
        self.start_button = tk.Button(self.buttons_frame, text="Check in", command=self.start_camera)
        self.start_button.pack(side=tk.LEFT, padx=30)

        # Create the "Stop" button
        self.stop_button = tk.Button(self.buttons_frame, text="Check out", command=self.stop_camera)
        self.stop_button.pack(side=tk.LEFT, padx=30)

        self.is_camera_running = False
        self.video_capture = None

    def start_camera(self):
        if not self.is_camera_running:
            # Open the video capture from the camera
            self.video_capture = cv2.VideoCapture(0)
            self.is_camera_running = True

            # Start the video update loop
            self.update_camera()

    def stop_camera(self):
        if self.is_camera_running:
            # Release the video capture
            self.video_capture.release()
            self.is_camera_running = False

    def update_camera(self):
        if self.is_camera_running:
            # Read a frame from the video capture
            ret, frame = self.video_capture.read()

            if ret:
                # Convert the OpenCV frame to PIL format
                image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                image = Image.fromarray(image)

                 # Resize the image to desired dimensions
                image = image.resize((500, 400))


                # Create an ImageTk object from the PIL image
                img_tk = ImageTk.PhotoImage(image)

                # Update the label with the new image
                self.label.imgtk = img_tk
                self.label.configure(image=img_tk)

        # Repeat the update after a delay (in milliseconds)
        self.window.after(10, self.update_camera)

# Create the Tkinter window
window = tk.Tk()

# Create the CameraApp instance
app = CameraApp(window)

# Run the Tkinter event loop
window.mainloop()
