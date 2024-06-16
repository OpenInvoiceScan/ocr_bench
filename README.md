# OCR Bench

This repository contains tools and scripts to evaluate and compare the performance of different OCR (Optical Character Recognition) technologies on invoice documents.

## Contents

- `facturas/`: Directory with invoice images used for testing.
- `legacy_code/`: Old code for reference.
- `collapse_lines.py`: Script to process and collapse lines in images.
- `easy_ocr.ipynb`: Jupyter Notebook for OCR using EasyOCR.
- `factura0.jpg`: Sample invoice image.
- `formatos_easy_ocr.txt`: Output formats for EasyOCR.
- `openCV.ipynb`: Jupyter Notebook for image processing using OpenCV.
- `renombrar_imagenes.sh`: Script to rename invoice images.
- `setup_venv.sh`: Script to set up a virtual environment.
- `tutorial.py`: Script with OCR usage examples.

## Usage

1. Clone the repository:
    ```bash
    git clone https://github.com/OpenInvoiceScan/ocr_bench.git
    ```
2. Set up the virtual environment:
    ```bash
    bash setup_venv.sh
    ```
3. Run the notebooks and scripts as needed to process images and perform OCR.
