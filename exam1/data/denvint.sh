# Ruta de la carpeta donde se encuentran los archivos .csv
carpeta="./data/denvint"

# Cambiar al directorio de la carpeta
cd "$carpeta"

# Bucle for para recorrer los archivos .csv
for i in *.csv; do
  echo "Archivo: $i"
  
  echo "Filas:"
  head -n1 "$i" | grep -o "," | wc -l
  
  echo "Columnas:" #NF variable que cuenta en cada archivo
  awk -F"," '{print NF}' "$i" | sort -nu | tail -n1
  
  echo "-----------------------------"
done



