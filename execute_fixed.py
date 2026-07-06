#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
sys.path.insert(0, '.')
from execute_notebooks import execute_and_save

# Ejecutar los notebooks corregidos
print('Ejecutando notebooks corregidos...')
execute_and_save('U5_bloque2_representacion_fixed.ipynb')
execute_and_save('U5_bloque3_densidad_fixed.ipynb')
