import cv2
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import numpy as np
import pytesseract

# Load Haar cascade
harcascade = "Car-Number-Plates-Detection-new\\Car-Number-Plates-Detection-main\\indian_license_plate.xml"
plate_cascade = cv2.CascadeClassifier(harcascade)

# Tesseract path
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\\tesseract.exe'

# Open image
def open_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg;*.png;*.jpeg")])
    if file_path:
        process_image(file_path)

# Process image
def process_image(file_path):
    img = cv2.imread(file_path)
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    plates = plate_cascade.detectMultiScale(img_gray, 1.1, 4)

    img_roi = None
    extracted_text = ""
    for (x, y, w, h) in plates:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
        cv2.putText(img, "", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 255), 2)
        
        img_roi = img_gray[y: y + h, x: x + w]
        cv2.imwrite("extracted_plate.jpg", img_roi)
        
        extracted_text = pytesseract.image_to_string(img_roi, config='--psm 8')
        save_text(extracted_text)
        break

    display_image(img, img_roi, extracted_text)

# Save text
def save_text(text):
    with open("detected_plate.txt", "w") as file:
        file.write(text.strip())

# Display in GUI
def display_image(img, img_roi, text):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = cv2.resize(img, (500, 330))  # Reduced size
    img = Image.fromarray(img)
    img = ImageTk.PhotoImage(img)
    panel.config(image=img)
    panel.image = img

    if img_roi is not None:
        roi_img = cv2.resize(img_roi, (300, 100))
        roi_img = Image.fromarray(roi_img)
        roi_img = ImageTk.PhotoImage(roi_img)
        roi_panel.config(image=roi_img)
        roi_panel.image = roi_img

    result_label.config(text=f"EXTRACTED NUMBER:\n{text.strip()}")

# Main GUI
root = tk.Tk()
root.title("Number Plate Detection")
root.geometry("900x750")
root.configure(bg="#e6f2ff")

heading = tk.Label(root, text="AUTOMATIC NUMBER PLATE DETECTION AND NUMBER EXTRACTION", font=("Helvetica", 18, "bold"), bg="#e6f2ff", fg="#003366")
heading.pack(pady=20)

btn = tk.Button(root, text="Upload Image", command=open_image, font=("Arial", 14, "bold"), bg="#0059b3", fg="white", padx=15, pady=5, relief="raised", bd=3)
btn.pack(pady=10)

# Frame for image display
img_frame = tk.Frame(root, bg="#ffffff", bd=2, relief="groove", padx=10, pady=10)
img_frame.pack(pady=10)

img_title = tk.Label(img_frame, text="UPLOADED IMAGE", font=("Arial", 14, "bold"), bg="#ffffff")
img_title.pack()
panel = tk.Label(img_frame, bg="#ffffff")
panel.pack()

# Frame for ROI display
roi_frame = tk.Frame(root, bg="#ffffff", bd=2, relief="groove", padx=10, pady=10)
roi_frame.pack(pady=10)

roi_title = tk.Label(roi_frame, text="EXTRACTED NUMBER PLATE", font=("Arial", 14, "bold"), bg="#ffffff")
roi_title.pack()
roi_panel = tk.Label(roi_frame, bg="#ffffff")
roi_panel.pack()

# Result frame
result_frame = tk.Frame(root, bg="#d1ecf1", bd=2, relief="groove", padx=20, pady=10)
result_frame.pack(pady=15)

result_label = tk.Label(result_frame, text="", font=("Courier", 16, "bold"), fg="#0c5460", bg="#d1ecf1", justify="center")
result_label.pack()

root.mainloop()
