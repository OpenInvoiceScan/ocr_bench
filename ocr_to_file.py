from PIL import Image
import pytesseract
import os
import argparse

# Recoger la ubicación de las imágenes
parser = argparse.ArgumentParser()
parser.add_argument("directory", help="Directorio de las imágenes")
args = parser.parse_args()

jpg_path = args.directory

img = Image.open(jpg_path)

text = pytesseract.image_to_string(img, lang='spa')

print(text)

