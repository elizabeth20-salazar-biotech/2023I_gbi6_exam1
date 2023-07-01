# 2.1
from Bio import Entrez
import csv

def fetch_species_info(accession):
    handle = Entrez.efetch(db="nucleotide", id=accession, rettype="gb", retmode="text")
    record = handle.read()
    handle.close()
    return record

def parse_species_info(record):
    species_info = {}
    for line in record.split("\n"):
        if line.startswith("  ORGANISM"):
            species_name = line.split("  ORGANISM")[1].strip()
            if species_name in species_info:
                species_info[species_name] += 1
            else:
                species_info[species_name] = 1
    return species_info

def save_species_info(species_info, filename):
    with open(filename, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Species", "Frequency"])
        for species, frequency in species_info.items():
            writer.writerow([species, frequency])

def main(accessions, filename):
    species_info = {}
    for accession in accessions:
        record = fetch_species_info(accession)
        species_info.update(parse_species_info(record))
    save_species_info(species_info, filename)
    print("Species information saved to", filename)

# Configura tus credenciales de NCBI
Entrez.email = "elizabeth.salazar@est.ikiam.edu.ec"

# Lista de accessions de las secuencias que deseas obtener información
accessions = ["NM_001276933", "NM_001276934", "NM_001276935"]

# Nombre del archivo de resultados
filename = "results/source.csv"

# Ejecuta el programa principal
main(accessions, filename)

#Ejercicio 2.2
import pandas as pd
import matplotlib.pyplot as plt
from Bio import Entrez, SeqIO
from Bio.SeqUtils.ProtParam import ProteinAnalysis

# Configuración de Entrez
Entrez.email = 'tu_email@example.com'  # Ingresa tu dirección de correo electrónico

# Obtener secuencia de ADN desde NCBI
def obtener_secuencia_ncbi(id_secuencia):
    handle = Entrez.efetch(db='nucleotide', id=id_secuencia, rettype='fasta', retmode='text')
    record = SeqIO.read(handle, 'fasta')
    return record.seq

# Obtener péptidos a partir de una secuencia de ADN
def obtener_peptidos(secuencia_adn):
    proteinas = []
    protein_seq = secuencia_adn.translate()
    for peptide in protein_seq.split('*'):
        if peptide.startswith('M'):
            proteinas.append(peptide)
    return proteinas

# Calcular peso molecular e índice de estabilidad
def calcular_propiedades(proteinas):
    resultados = []
    for proteina in proteinas:
        analysis = ProteinAnalysis(proteina)
        molecular_weight = analysis.molecular_weight()
        instability_index = analysis.instability_index()
        resultados.append((proteina, molecular_weight, instability_index))
    return resultados

# Guardar resultados en un archivo CSV
def guardar_resultados(resultados, filename):
    df = pd.DataFrame(resultados, columns=['Proteina', 'Peso Molecular', 'Indice de Estabilidad'])
    df.to_csv(filename, index=False)

# Generar gráfico joinplot
def generar_grafico(resultados):
    df = pd.DataFrame(resultados, columns=['Peso Molecular', 'Indice de Estabilidad'])
    plt.figure(figsize=(8, 6))
    plt.style.use('seaborn-whitegrid')
    plt.scatter(df['Peso Molecular'], df['Indice de Estabilidad'], s=60, color='purple', alpha=0.6)
    plt.xlabel('Peso Molecular')
    plt.ylabel('Indice de Estabilidad')
    plt.title('Relación entre Peso Molecular e Índice de Estabilidad')
    plt.savefig('results/glupeptides.png')
    plt.show()

# ID de la secuencia de ADN en NCBI (ejemplo: ID de la secuencia de la insulina humana)
secuencia_id = 'NM_000207.3'

# Obtener secuencia de ADN
secuencia_adn = obtener_secuencia_ncbi(secuencia_id)

# Obtener péptidos
proteinas = obtener_peptidos(secuencia_adn)

# Calcular propiedades
resultados = calcular_propiedades(proteinas)

# Guardar resultados en un archivo CSV
guardar_resultados(resultados, 'results/glupeptides.csv')

# Generar gráfico joinplot
generar_grafico(resultados)

