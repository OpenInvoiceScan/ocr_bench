from pdf2image import convert_from_path
import os

# Ruta del archivo PDF
pdf_paths = 'facturas'

# Encontrar todos los archivos PDF en la carpeta
pdf_paths = [os.path.join(pdf_paths, f) for f in os.listdir(pdf_paths) if f.endswith('.pdf')]
print(pdf_paths)

# Convertir en imagen los archivos PDF con sus respectivos nombres
for pdf_path in pdf_paths:
    images = convert_from_path(pdf_path, dpi=400)
    for i, image in enumerate(images):
        image.save(f'facturas/{pdf_path.split("/")[-1].split(".")[0]}.jpg', 'JPEG')

#images = convert_from_path(pdf_path)

# Guardar cada página como una imagen
#for i, image in enumerate(images):
    #image.save(f'pagina_{i}.jpg', 'JPEG')
