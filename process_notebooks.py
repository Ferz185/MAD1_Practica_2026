import json
import os
import sys
import subprocess
import numpy as np
import pandas as pd
from datetime import datetime
import io
import sys

# Configurar UTF-8 para Windows
if sys.stdout.encoding != 'utf-8':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# Lista de notebooks a procesar
notebooks = [
    'U5_bloque1_clustering.ipynb',
    'U5_bloque2_representacion.ipynb', 
    'U5_bloque3_densidad.ipynb',
    'U5_bloque4_autoencoders.ipynb'
]

notebooks_dir = r'Unidad 5'

def execute_notebook_and_complete(notebook_name):
    """
    Ejecuta un notebook y lo completa con respuestas
    """
    notebook_path = os.path.join(notebooks_dir, notebook_name)
    
    print(f"\n{'='*70}")
    print(f"Procesando: {notebook_name}")
    print(f"{'='*70}")
    
    # Leer el notebook
    with open(notebook_path, 'r', encoding='utf-8') as f:
        notebook = json.load(f)
    
    print(f"✓ Notebook cargado")
    print(f"  Total de celdas: {len(notebook['cells'])}")
    
    # Usar nbconvert para ejecutar
    output_path = os.path.join(notebooks_dir, notebook_name.replace('.ipynb', '_executed.ipynb'))
    
    try:
        print(f"\n→ Ejecutando notebook con nbconvert...")
        result = subprocess.run(
            ['python', '-m', 'jupyter', 'nbconvert', 
             '--to', 'notebook', 
             '--execute',
             '--ExecutePreprocessor.timeout=300',
             '--output', output_path,
             notebook_path],
            capture_output=True,
            text=True,
            timeout=600
        )
        
        if result.returncode != 0:
            print(f"⚠ Error al ejecutar: {result.stderr}")
        else:
            print(f"✓ Notebook ejecutado correctamente")
            print(f"  Salida guardada en: {output_path}")
            
            # Verificar que el archivo existe
            if os.path.exists(output_path):
                with open(output_path, 'r', encoding='utf-8') as f:
                    executed_nb = json.load(f)
                print(f"  ✓ Archivo de salida verificado")
                return executed_nb
            
    except subprocess.TimeoutExpired:
        print(f"✗ Timeout al ejecutar el notebook")
    except Exception as e:
        print(f"✗ Error: {e}")
    
    return None

def add_completion_info(notebook_name):
    """
    Añade información sobre el estado de completitud del notebook
    """
    summary = {
        'U5_bloque1_clustering.ipynb': {
            'tema': 'Clustering - K-means, Jerárquico, DBSCAN, GMM',
            'contenido': ['K-means', 'Método del codo', 'Coeficiente de silueta', 'Clustering jerárquico', 'DBSCAN', 'GMM'],
            'temas_principales': 'Métodos de clustering no supervisado y comparativa'
        },
        'U5_bloque2_representacion.ipynb': {
            'tema': 'Representación de datos - PCA, t-SNE, UMAP',
            'contenido': ['PCA', 't-SNE', 'UMAP'],
            'temas_principales': 'Reducción de dimensionalidad lineal y no lineal'
        },
        'U5_bloque3_densidad.ipynb': {
            'tema': 'Densidad y Anomalías - KDE, Isolation Forest',
            'contenido': ['KDE', 'Isolation Forest', 'Detección de anomalías'],
            'temas_principales': 'Estimación de densidad y detección de outliers'
        },
        'U5_bloque4_autoencoders.ipynb': {
            'tema': 'Autoencoders - Arquitectura y aplicaciones',
            'contenido': ['Autoencoder lineal', 'Autoencoder convolucional', 'Detección de anomalías con AE'],
            'temas_principales': 'Deep learning no supervisado y compresión de datos'
        }
    }
    return summary.get(notebook_name, {})

# Procesar cada notebook
print("\n" + "="*70)
print("INICIANDO PROCESAMIENTO DE NOTEBOOKS UNIDAD 5")
print("="*70)

for notebook_name in notebooks:
    info = add_completion_info(notebook_name)
    print(f"\n[TEMA] {info.get('tema', 'N/A')}")
    
    executed = execute_notebook_and_complete(notebook_name)

print("\n" + "="*70)
print("PROCESAMIENTO COMPLETADO")
print("="*70)
