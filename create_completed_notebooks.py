#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import os
from pathlib import Path
import shutil

notebooks_executed = {
    'U5_bloque1_clustering': 'U5_bloque1_clustering_executed.ipynb',
    'U5_bloque2_representacion': 'U5_bloque2_representacion_executed.ipynb',
    'U5_bloque3_densidad': 'U5_bloque3_densidad_fixed_executed.ipynb',
    'U5_bloque4_autoencoders': 'U5_bloque4_autoencoders_executed.ipynb'
}

respuestas_tecnicas = {
    'U5_bloque1_clustering': [
        {
            'titulo': 'Conclusiones - Comparativa de Metodos de Clustering',
            'contenido': '''## Analisis Comparativo de Metodos de Clustering

### Hallazgos principales:

1. **K-means**: Excelente para clusters esfericos bien definidos, pero falla con formas complejas (como en el dataset de lunas).

2. **Clustering Jerarquico**: Flexible en cuanto a formas de clusters, es muy util para explorar dendogramas y entender estructuras jerarquicas.

3. **DBSCAN**: Ideal para clusters de formas irregulares y con capacidad de detectar outliers. Parametrizable por epsilon y min_samples.

4. **GMM (Gaussian Mixture Models)**: Probabilistico, proporciona probabilidades de asignacion a clusters.

### Seleccion del metodo:
- Datos esfericos bien definidos → K-means
- Estructura jerarquica importante → Clustering jerarquico
- Formas arbitrarias, outliers → DBSCAN
- Probabilidades de asignacion → GMM

### Recomendaciones practicas:
- Validar con metodo del codo y coeficiente de silueta
- Visualizar resultados en 2D/3D cuando sea posible
- Considerar multiples valores de k/epsilon antes de decidir'''
        }
    ],
    'U5_bloque2_representacion': [
        {
            'titulo': 'Conclusiones - Reduccion de Dimensionalidad',
            'contenido': '''## Analisis de Tecnicas de Reduccion Dimensional

### Metodos explorados:

1. **PCA (Analisis de Componentes Principales)**:
   - Lineal, preserva maxima varianza
   - Velocidad: muy rapida
   - Interpretabilidad: excelente (componentes principales)
   - Desventaja: no preserva estructura local

2. **t-SNE (t-Distributed Stochastic Neighbor Embedding)**:
   - No lineal, preserva estructura local
   - Excelente visualizacion de clusters
   - Puede ser lenta en datasets grandes
   - Desventaja: distancias no interpretables, computacionalmente costosa

3. **UMAP (Uniform Manifold Approximation and Projection)**:
   - No lineal, mas rapido que t-SNE
   - Preserva mejor la estructura global
   - Escala mejor a datasets grandes
   - Equilibrio entre velocidad e interpretabilidad

### Cuando usar cada uno:
- Exploracion inicial → PCA
- Visualizacion de clusters → t-SNE o UMAP
- Datasets grandes → UMAP
- Machine learning posterior → PCA o componentes de UMAP

### Parametros criticos:
- PCA: n_components (varianza explicada)
- t-SNE: perplejidad (recomendado 30-50)
- UMAP: n_neighbors, min_dist'''
        }
    ],
    'U5_bloque3_densidad': [
        {
            'titulo': 'Conclusiones - Estimacion de Densidad y Anomalias',
            'contenido': '''## Metodos de Densidad y Deteccion de Anomalias

### KDE (Kernel Density Estimation):
- Estimacion suave de densidad de probabilidad
- Parametro bandwidth: controla suavidad
- Ventajas: interpretable, flexible
- Desventajas: curse of dimensionality

### Isolation Forest:
- Ensemble de arboles aislados
- No requiere calcular distancias
- Excelente para espacios de alta dimension
- Ventajas: eficiente, no lineal
- Particularmente efectivo para outliers globales

### Deteccion de Anomalias:
1. Enfoque supervisado: entrenar con datos "normales"
2. Enfoque no supervisado: detectar puntos atipicos
3. Hibrido: combinar multiples metodos

### Aplicacion a datos reales (Breast Cancer):
- Precision/Recall vs umbral
- ROC-AUC para evaluar rendimiento
- Interpretabilidad biologica de anomalias'''
        }
    ],
    'U5_bloque4_autoencoders': [
        {
            'titulo': 'Conclusiones - Autoencoders y Deep Learning No Supervisado',
            'contenido': '''## Autoencoders: Teoria y Practica

### Arquitectura:
- Encoder: comprime datos de alta dimension
- Bottleneck: representacion latente compacta
- Decoder: reconstruye datos originales

### Tipos explorados:
1. Autoencoder Lineal: equivalente a PCA pero con capacidad de optimizacion neural
2. Autoencoder Convolucional: para datos con estructura espacial (imagenes)

### Aplicaciones:
1. **Compresion de datos**: reducir dimensionalidad preservando informacion
2. **Deteccion de anomalias**: error de reconstruccion alto = anomalia
3. **Denoising**: entrenar con datos ruidosos como entrada, limpios como salida

### Ventajas vs PCA:
- Capacidad no lineal
- Flexibility arquitectonica
- Escalable a grandes datasets con GPU
- Combinable con otras tecnicas de deep learning

### Desafios practicos:
- Seleccion de tamano del bottleneck
- Overfitting si bottleneck es muy grande
- Requiere experiencia en tuning de hiperparametros
- Computational cost inicial mayor pero amortizado en produccion'''
        }
    ]
}

def add_conclusion_cell(nb, title, content):
    """Anade una celda markdown de conclusion al notebook"""
    conclusion_cell = {
        "cell_type": "markdown",
        "metadata": {},
        "source": [f"## {title}\n\n{content}"]
    }
    nb['cells'].append(conclusion_cell)

# Main
print("=" * 70)
print("CREANDO VERSIONES COMPLETADAS DE NOTEBOOKS")
print("=" * 70)

notebooks_dir = Path('Unidad 5')

for nombre_base, archivo_ejecutado in notebooks_executed.items():
    print(f"\n[PROCESANDO] {nombre_base}")
    
    input_path = notebooks_dir / archivo_ejecutado
    output_path = notebooks_dir / f"{nombre_base}_completado.ipynb"
    
    if not input_path.exists():
        print(f"  [ERROR] Archivo no encontrado: {input_path}")
        continue
    
    try:
        # Leer el notebook ejecutado
        with open(input_path, 'r', encoding='utf-8') as f:
            nb = json.load(f)
        
        # Anadir respuestas tecnicas
        if nombre_base in respuestas_tecnicas:
            for answer in respuestas_tecnicas[nombre_base]:
                add_conclusion_cell(nb, answer['titulo'], answer['contenido'])
        
        # Guardar la version completada
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(nb, f, indent=1, ensure_ascii=False)
        
        print(f"  [OK] Guardado: {output_path}")
        
    except Exception as e:
        print(f"  [ERROR] {type(e).__name__}: {e}")

print("\n" + "=" * 70)
print("COMPLETADO")
print("=" * 70)
