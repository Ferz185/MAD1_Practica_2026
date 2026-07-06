#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
from pathlib import Path

nb_path = Path('Unidad 5') / 'U5_bloque2_representacion.ipynb'

print("[PROCESANDO] Corrigiendo todas las instancias de n_iter...")

with open(nb_path, 'r', encoding='utf-8') as f:
    nb = json.load(f)

corrections = 0
for cell in nb['cells']:
    if cell.get('cell_type') == 'code':
        source = ''.join(cell.get('source', []))
        
        if 'n_iter=' in source:
            new_source = source.replace('n_iter=', 'max_iter=')
            cell['source'] = new_source
            corrections += 1

print(f"[OK] Corregidas {corrections} celdas")

# Guardar
output_path = Path('Unidad 5') / 'U5_bloque2_representacion_fixed.ipynb'
with open(output_path, 'w', encoding='utf-8') as f:
    json.dump(nb, f, indent=1, ensure_ascii=False)

print(f"[OK] Guardado: {output_path}")
