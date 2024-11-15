import cv2
import tkinter as tk
from tkinter import ttk
import PIL.Image, PIL.ImageTk
import numpy as np
from pathlib import Path


class FaceDetectionApp:
    def __init__(self, window):
        self.window = window
        self.window.title("Face Detection App")

        # Load the face detection cascade classifier
        cascade_path = cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
        self.face_cascade = cv2.CascadeClassifier(cascade_path)

        # Initialize video capture
        self.cap = cv2.VideoCapture(0)

        # Create GUI elements
        self.create_widgets()

        # Initialize detection status
        self.detection_status = "No face detected"

        # Start video loop
        self.update_frame()

    def create_widgets(self):
        # Create main frame
        self.main_frame = ttk.Frame(self.window, padding="10")
        self.main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Create canvas for video display
        self.canvas = tk.Canvas(self.main_frame, width=640, height=480)
        self.canvas.grid(row=0, column=0, pady=5)

        # Create status label
        self.status_label = ttk.Label(
            self.main_frame,
            text=self.detection_status,
            font=('Arial', 24, 'bold')
        )
        self.status_label.grid(row=1, column=0, pady=10)

    def detect_faces(self, frame):
        # Convert frame to grayscale for face detection
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detect faces
        faces = self.face_cascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30)
        )

        # Update detection status
        if len(faces) > 0:
            self.detection_status = "Face detected"
            # Draw rectangles around detected faces
            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        else:
            self.detection_status = "No face detected"

        return frame

    def update_frame(self):
        # Read frame from camera
        ret, frame = self.cap.read()

        if ret:
            # Flip frame horizontally for mirror effect
            frame = cv2.flip(frame, 1)

            # Perform face detection
            frame = self.detect_faces(frame)

            # Convert frame to RGB for tkinter
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            # Convert to PhotoImage
            self.photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame_rgb))

            # Update canvas and status label
            self.canvas.create_image(0, 0, image=self.photo, anchor=tk.NW)
            self.status_label.configure(text=self.detection_status)

        # Schedule next update
        self.window.after(10, self.update_frame)

    def cleanup(self):
        self.cap.release()


def main():
    # Create main window
    root = tk.Tk()
    root.title("Face Detection App")

    # Create app instance
    app = FaceDetectionApp(root)

    # Set cleanup on window close
    root.protocol("WM_DELETE_WINDOW", lambda: [app.cleanup(), root.destroy()])

    # Start main loop
    root.mainloop()


if __name__ == "__main__":
    main()