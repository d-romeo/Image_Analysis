# Image_Analysis
# License Plate Recognition Access Control System

Welcome to the License Plate Recognition Access Control System project! This project aims to automate access control by identifying vehicles based on their license plates. When a vehicle approaches a gate, the system captures an image of the vehicle's license plate, extracts the license plate number from the image, and grants access if the number is in a predefined list of accepted license plates.

## Features

- **Automatic Image Capture**: The system captures an image of the vehicle when it arrives at the gate.
- **License Plate Detection**: It extracts the license plate number from the captured image.
- **Text Recognition**: Utilizes Tesseract OCR to recognize text from the license plate.
- **Access Control**: Compares the recognized license plate number with a predefined list of accepted license plates and grants or denies access accordingly.

## Requirements

- Python 3.x
- OpenCV
- Tesseract OCR
- pytesseract
- numpy

## Installation

1. **Clone the repository**
    ```sh
    git clone https://github.com/yourusername/Image_Analysis.git
    cd license-plate-recognition-access-control
    ```

2. **Install the required Python packages**
    ```sh
    pip install -r requirements.txt
    ```

3. **Install Tesseract OCR**
    - **Windows**: Download the installer from [Tesseract at UB Mannheim](https://github.com/UB-Mannheim/tesseract/wiki) and follow the installation instructions.
    - **macOS**: Use Homebrew
        ```sh
        brew install tesseract
        ```
    - **Linux**: Use your package manager
        ```sh
        sudo apt-get install tesseract-ocr
        ```

## Usage

1. **Run the access control system**
    ```sh
    python gui.py
    ```

2. **Using the GUI**:
    - Launching `gui.py` will open the graphical user interface (GUI).
    - Use the interface to add accepted license plates manually.
    - The system will select a license plate image randomly from the `plates` directory.
    - When a vehicle arrives, the system captures an image of the vehicle and processes it to detect and recognize the license plate.
    - The recognized license plate number is checked against the list of accepted license plates entered through the GUI.
    - If the license plate number is accepted, access is granted; otherwise, access is denied.

## Contributing

Contributions are welcome! Please fork this repository, make your changes, and submit a pull request.

## Acknowledgments

- [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) for their powerful OCR engine.
- [OpenCV](https://opencv.org/) for providing an excellent computer vision library.

Thank you for using the License Plate Recognition Access Control System!