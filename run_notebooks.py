#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import os
import subprocess
import sys

# Lista de notebooks
notebooks = [
    'U5_bloque1_clustering.ipynb',
    'U5_bloque2_representacion.ipynb', 
    'U5_bloque3_densidad.ipynb',
    'U5_bloque4_autoencoders.ipynb'
]

notebooks_dir = r'Unidad 5'

def execute_notebook(notebook_name):
    """Ejecuta un notebook con Jupyter"""
    notebook_path = os.path.join(notebooks_dir, notebook_name)
    output_path = os.path.join(notebooks_dir, notebook_name.replace('.ipynb', '_executed.ipynb'))
    
    print(f"\n[PROCESANDO] {notebook_name}")
    print("=" * 60)
    
    try:
        # Verificar que el archivo existe
        if not os.path.exists(notebook_path):
            print(f"ERROR: No se encontro {notebook_path}")
            return False
        
        # Ejecutar con subprocess
        cmd = [
            sys.executable, '-m', 'jupyter', 'nbconvert',
            '--to', 'notebook',
            '--execute',
            '--ExecutePreprocessor.timeout=300',
            '--output', output_path,
            notebook_path
        ]
        
        print(f"Ejecutando: {' '.join(cmd)}")
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=600)
        
        if result.returncode == 0:
            print(f"[OK] Notebook ejecutado correctamente")
            if os.path.exists(output_path):
                print(f"[OK] Salida guardada en: {output_path}")
                return True
        else:
            print(f"[ERROR] stdout: {result.stdout}")
            print(f"[ERROR] stderr: {result.stderr}")
            
    except subprocess.TimeoutExpired:
        print(f"[TIMEOUT] El notebook tardo demasiado")
    except Exception as e:
        print(f"[ERROR] {type(e).__name__}: {e}")
    
    return False

# Main
print("=" * 60)
print("PROCESAMIENTO DE NOTEBOOKS - UNIDAD 5")
print("=" * 60)

results = {}
for notebook in notebooks:
    results[notebook] = execute_notebook(notebook)

print("\n" + "=" * 60)
print("RESUMEN")
print("=" * 60)
for nb, success in results.items():
    status = "OK" if success else "FALLO"
    print(f"[{status}] {nb}")
