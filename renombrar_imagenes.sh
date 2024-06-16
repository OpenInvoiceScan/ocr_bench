#!/bin/bash

# Contador inicial
contador=1

# Iterar sobre todos los archivos .jpg en el directorio actual
for archivo in *.jpg; do
  # Renombrar archivo
  mv "$archivo" "imagen${contador}.jpg"
  # Incrementar contador
  contador=$((contador + 1))
done
