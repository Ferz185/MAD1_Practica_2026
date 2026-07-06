#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import os
import sys
from pathlib import Path

# Importar nbconvert
try:
    from nbconvert import PythonExporter, NotebookExporter
    from nbconvert.preprocessors import ExecutePreprocessor
    import nbformat
    print("[OK] nbconvert y nbformat importados correctamente")
except ImportError as e:
    print(f"[ERROR] No se pudo importar: {e}")
    print("Instalando dependencias...")
    import subprocess
    subprocess.run([sys.executable, '-m', 'pip', 'install', '-q', 'nbconvert', 'nbformat'])
    from nbconvert import PythonExporter, NotebookExporter
    from nbconvert.preprocessors import ExecutePreprocessor
    import nbformat

notebooks = [
    'U5_bloque1_clustering.ipynb',
    'U5_bloque2_representacion.ipynb', 
    'U5_bloque3_densidad.ipynb',
    'U5_bloque4_autoencoders.ipynb'
]

notebooks_dir = Path(r'Unidad 5')

def execute_and_save(notebook_name):
    """Ejecuta un notebook y guarda la salida"""
    nb_path = notebooks_dir / notebook_name
    output_path = notebooks_dir / notebook_name.replace('.ipynb', '_executed.ipynb')
    
    print(f"\n[PROCESANDO] {notebook_name}")
    print("=" * 60)
    
    try:
        # Leer el notebook
        with open(nb_path, 'r', encoding='utf-8') as f:
            nb = nbformat.read(f, as_version=4)
        
        print(f"[OK] Notebook leido: {len(nb.cells)} celdas")
        
        # Ejecutar el notebook
        ep = ExecutePreprocessor(timeout=300, kernel_name='python3')
        
        print("Ejecutando celdas...")
        executed_nb, _ = ep.preprocess(nb, {'metadata': {'path': str(notebooks_dir)}})
        
        # Guardar el resultado
        with open(output_path, 'w', encoding='utf-8') as f:
            nbformat.write(executed_nb, f)
        
        print(f"[OK] Notebook guardado: {output_path}")
        return True
        
    except Exception as e:
        print(f"[ERROR] {type(e).__name__}: {e}")
        return False

# Main
print("=" * 60)
print("EJECUCION DE NOTEBOOKS - UNIDAD 5")
print("=" * 60)

results = {}
for notebook in notebooks:
    results[notebook] = execute_and_save(notebook)

print("\n" + "=" * 60)
print("RESUMEN")
print("=" * 60)
for nb, success in results.items():
    status = "OK" if success else "FALLO"
    print(f"[{status}] {nb}")
