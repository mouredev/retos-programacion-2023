#!/bin/bash

filename="text.txt"

if [ ! -e "$filename" ]; then
  touch "$filename"
fi

echo "Bienvenido al programa de edición de texto."
echo "Selecciona una opción:"
echo "1. Agregar texto"
echo "2. Borrar contenido y empezar desde el principio"
read option

case $option in
  1)
	cat "$filename"
    echo "Introduce el texto (presiona Ctrl+D para finalizar):"
    cat >> "$filename"
    ;;
  2)
    > "$filename"
    echo "Contenido borrado. Introduce el nuevo texto:"
    cat >> "$filename"
    ;;
  *)
    echo "Opción no válida."
    ;;
esac

echo "Contenido actual del archivo:"
cat "$filename"

