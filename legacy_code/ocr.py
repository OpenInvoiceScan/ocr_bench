from PIL import Image
import pytesseract
import os

# Definir la ubicación de las imágenes
jpg_paths = 'facturas'

# Encontrar todos los archivos JPG en la carpeta
jpg_paths = [os.path.join(jpg_paths, f) for f in os.listdir(jpg_paths) if f.endswith('.jpg')]
print(jpg_paths)

# Leer y aplicar OCR a cada imagen
for jpg_path in jpg_paths:
    img = Image.open(jpg_path)

    # Tesseract maneja bien varios modos de imagen, pero la conversión a escala de grises puede mejorar la precisión
    if img.mode != 'L':
        img = img.convert('L')

    # Aplicar OCR usando Tesseract
    text = pytesseract.image_to_string(img, lang='spa')  # Asegúrate de tener instalados los idiomas necesarios

    print(text)

    # Guardar el texto extraído en un archivo
    with open(f'facturas/{jpg_path.split("/")[-1].split(".")[0]}.txt', 'w') as f:
        f.write(text)
    f.close()
