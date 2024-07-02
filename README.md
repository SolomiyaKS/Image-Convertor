# Image-Convertor
_____
## Overview
Image Converter is a simple desktop application built with Python and PyQt6 that allows users to convert images between various formats. The application supports formats like PNG, JPEG, and JPG. It provides a user-friendly interface to browse and select images and choose the desired output format for conversion.

## Features 
- Browse and select image files
- Convert images to different formats (PNG, JPEG, JPG)
- Automatic conversion of RGBA images to RGB when saving as JPEG/JPG
- Simple and intuitive user interface
- Error handling and informative messages

## Requirements
- Python 3.7+
- PyQt6
- Pillow (PIL Fork)
_______

## Installation
1. Clone the repository:
   ```
   git clone https://github.com/your-username/image-converter.git
   cd image-converter
   ```
2. Create a virtual environment (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate
   ```
3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```
_____
## Structure 
```
image-converter/
│
├── main.py         # Main application script
├── main.ui         # UI file created with Qt Designer
├── style.qss       # Custom stylesheet for the application
├── requirements.txt# List of dependencies
└── README.md       # Project README file
```
- ### main.ui
  The main.ui file contains the layout and design of the application's user interface, created with Qt Designer.
- ### style.qss
  The style.qss file contains custom styles for the application to enhance the visual appearance.
  
