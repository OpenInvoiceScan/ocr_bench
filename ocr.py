import pytesseract
from PIL import Image

# Especifica la ruta al ejecutable de Tesseract si no está en el PATH
pytesseract.pytesseract.tesseract_cmd = r'/bin/tesseract'



# Leer y aplicar OCR a cada imagen):
    # Cargar la imagen
img = Image.open('pagina_0.jpg')
    
# Aplicar OCR
text = pytesseract.image_to_string(img, lang='spa')

# Imprimir o guardar el texto extraído
print(text)