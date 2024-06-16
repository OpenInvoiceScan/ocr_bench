import easyocr
import numpy as np
import time

def detect_tables(result, y_threshold=10):
    """
    Detecta posibles tablas en el resultado de EasyOCR basado en la alineación vertical de los bounding boxes.
    
    :param result: Resultado de easyocr.Reader.readtext.
    :param y_threshold: Umbral de diferencia en y para considerar que dos textos están en la misma fila.
    :return: Lista de tablas detectadas, cada tabla es una lista de filas, y cada fila es una lista de palabras.
    """
    lines = []
    current_line = []
    last_y = None
    
    for (box, text, prob) in result:
        # Obtener la coordenada y del centro del bounding box
        y_center = np.mean([oint[1] for oint in box])
        if last_y is None or abs(y_center - last_y) < y_threshold:
            current_line.append((box, text, prob))
        else:
            lines.append(current_line)
            current_line = [(box, text, prob)]
        last_y = y_center
    
    if current_line:
        lines.append(current_line)
    
    return lines

def group_texts_by_proximity(result, max_distance=20):
    """
    Agrupa las palabras basadas en la proximidad de sus bounding boxes.
    
    :param result: Resultado de easyocr.Reader.readtext.
    :param max_distance: Distancia máxima en píxeles para considerar que dos palabras están en el mismo grupo.
    :return: Lista de grupos de palabras.
    """
    def distance(box1, box2):
        """
        Calcula la distancia entre dos bounding boxes.
        """
        center1 = np.mean(box1, axis=0)
        center2 = np.mean(box2, axis=0)
        return np.linalg.norm(center1 - center2)
    
    groups = []
    for (box, text, prob) in result:
        added = False
        for group in groups:
            if any(distance(box, gbox) < max_distance for gtext, gbox, gprob in group):
                group.append((text, box, prob))
                added = True
                break
        if not added:
            groups.append([(text, box, prob)])
    
    return groups

# Configurar el lector de EasyOCR
time_start = time.time()

reader = easyocr.Reader(['en'], gpu=True)
time_end = time.time() - time_start

print(f"Tiempo de ejecución: {time_end} s")


# Leer la imagen


result = reader.readtext('facturas/1c67acf5-7c45-490d-a798-72051f431b38.jpg', )



# Detectar tablas
lines = detect_tables(result)


# Agrupar las líneas de las tablas y el texto restante
grouped_texts = []
for line in lines:
    if len(line) > 1:  # Considerar líneas con más de un elemento como parte de una tabla
        line_text = " ".join([text for box, text, prob in line])
        grouped_texts.append(line_text)
    else:
        # Agrupar el texto restante por proximidad
        groups = group_texts_by_proximity(line)
        grouped_texts.extend([" ".join([text for text, box, prob in group]) for group in groups])

# Imprimir los textos agrupados
for i, group_text in enumerate(grouped_texts):
    print(f"Grupo {i + 1}: {group_text}")
