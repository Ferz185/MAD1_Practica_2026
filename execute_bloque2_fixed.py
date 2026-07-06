#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import nbformat
from nbconvert.preprocessors import ExecutePreprocessor
from pathlib import Path

nb_path = Path('Unidad 5') / 'U5_bloque2_representacion_fixed.ipynb'
output_path = Path('Unidad 5') / 'U5_bloque2_representacion_executed.ipynb'

print("[EJECUTANDO] U5_bloque2_representacion_fixed.ipynb")

try:
    with open(nb_path, 'r', encoding='utf-8') as f:
        nb = nbformat.read(f, as_version=4)
    
    ep = ExecutePreprocessor(timeout=300, kernel_name='python3')
    executed_nb, _ = ep.preprocess(nb, {'metadata': {'path': str(Path('Unidad 5'))}})
    
    with open(output_path, 'w', encoding='utf-8') as f:
        nbformat.write(executed_nb, f)
    
    print(f"[OK] Guardado: {output_path}")
    
except Exception as e:
    print(f"[ERROR] {type(e).__name__}: {e}")
