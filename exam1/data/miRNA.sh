#!/bin/bashdata/miRNA.dat

# Contar el número total de artículos
total_articulos=$(grep -c "PUBMED" data/miRNA.dat)
echo "Número total de artículos: $total_articulos"

# Contar el número de estudios de micro RNA en la revista Nature
nature_estudios=$(grep -c "Nature" data/miRNA.dat)
echo "Número de estudios en la revista Nature: $nature_estudios"

# Contar el número de estudios de micro RNA en la revista Nature con organismo C. elegans
elegans_estudios=$(grep -c "Nature, Caenorhabditis elegans*" data/miRNA.dat)
echo "Número de estudios en la revista Nature con organismo C. elegans: $elegans_estudios"

# Contar el número de micro RNA estudiados con una longitud de 139 pares de bases
grep "139 BP" data/miRNA.dat > elegans.txt
num_mirna_139=$(grep -c "139 BP" elegans.txt)
echo "Número de micro RNA estudiados con longitud 139 pares de bases: $num_mirna_139"
