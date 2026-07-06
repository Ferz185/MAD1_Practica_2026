#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import os
from pathlib import Path

# Corregir y completar notebooks

def fix_and_complete_bloque2():
    """Corrige el notebook de bloque 2 (t-SNE) y lo completa"""
    nb_path = Path('Unidad 5') / 'U5_bloque2_representacion.ipynb'
    
    print("\n[PROCESANDO] U5_bloque2_representacion.ipynb")
    
    with open(nb_path, 'r', encoding='utf-8') as f:
        nb = json.load(f)
    
    # Buscar la celda de t-SNE y corregir el parametro
    for cell in nb['cells']:
        if cell.get('cell_type') == 'code':
            source = ''.join(cell.get('source', []))
            
            # Corregir n_iter -> max_iter
            if 'n_iter=1000' in source:
                new_source = source.replace('n_iter=1000', 'max_iter=1000')
                cell['source'] = new_source.split('\n')
                print(f"[CORREGIDO] Cambio n_iter a max_iter")
    
    # Guardar
    output_path = Path('Unidad 5') / 'U5_bloque2_representacion_fixed.ipynb'
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(nb, f, indent=1, ensure_ascii=False)
    
    print(f"[OK] Guardado: {output_path}")
    return str(output_path)

def fix_and_complete_bloque3():
    """Corrige el notebook de bloque 3 (Isolation Forest) y lo completa"""
    nb_path = Path('Unidad 5') / 'U5_bloque3_densidad.ipynb'
    
    print("\n[PROCESANDO] U5_bloque3_densidad.ipynb")
    
    with open(nb_path, 'r', encoding='utf-8') as f:
        nb = json.load(f)
    
    # Buscar la celda de threshold_ y corregirla
    for cell in nb['cells']:
        if cell.get('cell_type') == 'code':
            source = ''.join(cell.get('source', []))
            
            # Corregir threshold_ por offset_
            if 'iso.threshold_' in source:
                new_source = source.replace('iso.threshold_', 'iso.offset_')
                cell['source'] = new_source.split('\n')
                print(f"[CORREGIDO] Cambio threshold_ a offset_")
    
    # Guardar
    output_path = Path('Unidad 5') / 'U5_bloque3_densidad_fixed.ipynb'
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(nb, f, indent=1, ensure_ascii=False)
    
    print(f"[OK] Guardado: {output_path}")
    return str(output_path)

# Main
print("=" * 70)
print("CORRIGIENDO NOTEBOOKS CON ERRORES")
print("=" * 70)

fixed_files = []
fixed_files.append(fix_and_complete_bloque2())
fixed_files.append(fix_and_complete_bloque3())

print("\n" + "=" * 70)
print(f"Archivos corregidos guardados:")
for f in fixed_files:
    print(f"  - {f}")
print("=" * 70)
