#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
from pathlib import Path

notebooks_dir = Path('Unidad 5')
completed_files = [
    'U5_bloque1_clustering_completado.ipynb',
    'U5_bloque2_representacion_completado.ipynb',
    'U5_bloque3_densidad_completado.ipynb',
    'U5_bloque4_autoencoders_completado.ipynb'
]

print("=" * 70)
print("VERIFICACION DE NOTEBOOKS COMPLETADOS")
print("=" * 70)

for nb_file in completed_files:
    nb_path = notebooks_dir / nb_file
    
    if not nb_path.exists():
        print(f"\n[ERROR] {nb_file} no existe")
        continue
    
    with open(nb_path, 'r', encoding='utf-8') as f:
        nb = json.load(f)
    
    # Contar celdas
    total_cells = len(nb['cells'])
    code_cells = sum(1 for c in nb['cells'] if c['cell_type'] == 'code')
    markdown_cells = sum(1 for c in nb['cells'] if c['cell_type'] == 'markdown')
    
    # Buscar conclusiones
    has_conclusion = any('Conclusiones' in ''.join(c.get('source', [])) 
                         for c in nb['cells'] if c['cell_type'] == 'markdown')
    
    # Buscar outputs
    has_outputs = any(c.get('outputs', []) for c in nb['cells'] if c['cell_type'] == 'code')
    
    print(f"\n[OK] {nb_file}")
    print(f"  Total cells: {total_cells}")
    print(f"  Code cells: {code_cells}")
    print(f"  Markdown cells: {markdown_cells}")
    print(f"  Has conclusions: {'Si' if has_conclusion else 'No'}")
    print(f"  Has outputs: {'Si' if has_outputs else 'No'}")
    print(f"  File size: {nb_path.stat().st_size / 1024:.1f} KB")

print("\n" + "=" * 70)
print("VERIFICACION COMPLETADA")
print("=" * 70)
