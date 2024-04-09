from pdf2image import convert_from_path

# Ruta del archivo PDF
pdf_path = 'factura0.pdf'

# Convertir el PDF en una lista de imágenes
images = convert_from_path(pdf_path)

# Guardar cada página como una imagen
for i, image in enumerate(images):
    image.save(f'pagina_{i}.jpg', 'JPEG')
