# Car-Number-Plates-Detection-And-Number-Extraction
🛑 Automatic Number Plate Detection and Text Extraction
This Python project uses OpenCV, Haar Cascade, and Tesseract OCR to detect vehicle number plates from an uploaded image and extract the text written on the plate. A simple GUI is built using Tkinter to interact with the tool.

🚀 Features
Upload an image of a vehicle.

<img width="1120" alt="image" src="https://github.com/user-attachments/assets/5c085cd7-8ae2-4a2a-89a8-8a425ad7ba1b" />

Detect number plate using Haar Cascade classifier.

Extract number plate region using OpenCV.

Recognize text from the plate using Tesseract OCR.

Display the full image, extracted plate, and extracted text in a user-friendly GUI.

Save extracted text to a local .txt file.

🛠 Tech Stack
Python 3

OpenCV

Pillow (PIL)

Pytesseract (OCR)

Tkinter (GUI)

📂 Folder Structure
project-root/
├── Car-Number-Plates-Detection-main/
│   └── indian_license_plate.xml   # Haar Cascade for plate detection
├── main.py                        # GUI and detection logic
├── extracted_plate.jpg            # Saved cropped plate image
└── detected_plate.txt             # Saved extracted number text


📸 Sample Use-Case
Upload an image like car.jpg

Plate is detected and highlighted

Cropped number plate is displayed

Text such as MH12AB1234 is extracted and shown

![Screenshot 2025-04-23 124709](https://github.com/user-attachments/assets/76dce595-030a-4cf2-96a8-365a49e1fc00)


