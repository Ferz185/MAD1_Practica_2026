# MAD1_Practica_2026 - Parte Práctica

Repositorio oficial de ejercicios prácticos y análisis de datos para la materia **Métodos para el Análisis de Datos I (MAD1)** - 2026.

## Descripción General

Este repositorio contiene guías, ejercicios, notebooks Jupyter y datasets utilizados para la parte práctica del curso. Los estudiantes trabajarán con técnicas de análisis exploratorio (EDA), clustering, visualización de datos y exportación de resultados.

## Estructura del Repositorio

```
.
├── Unidad 1/          # Introducción a Python y análisis básico de datos
├── Unidad 2 y 3/      # Análisis exploratorio, regresión lineal y polinómica.
├── Unidad 4/          # Métodos de aprendizaje supervisado (árboles, RF, SVM, KNN, redes)
└── Unidad 5/          # Análisis completo: EDA, clustering y conclusiones
    ├── alfajores_dataset.csv           # Dataset sintético (120 registros)
    ├── U5_alfajores_analisis.ipynb     # Notebook completo con análisis
    └── alfajores_analisis_resultados.csv # Asignaciones de clusters y features
```

## Observaciones para la unidad 5: Caso de Estudio - Análisis de Alfajores

### Objetivo
Demostrar un pipeline completo de análisis de datos: desde carga y exploración, hasta segmentación (clustering) con K-Means y exportación de resultados.

### Contenido del Análisis

1. **Carga y Exploración (EDA)**
   - Descripción del dataset (n=120 registros, 6 marcas, 6 tipos de relleno)
   - Estadísticas descriptivas y distribuciones
   - Visualizaciones: scatterplots, histogramas, boxplots, correlaciones

2. **Limpieza y Preparación**
   - Codificación de variables categóricas
   - Escalado de features numéricas (StandardScaler)

3. **Clustering (K-Means)**
   - Selección automática de k óptimo mediante **silhouette score** (evaluación en rango 2-6)
   - Entrenamiento de KMeans con n_init=10 y seed=42
   - Visualización de clusters en 2D con **PCA**

4. **Interpretación y Resultados**
   - Centroides en escala original
   - Cruces cluster vs. tipo de relleno
   - Resumen estadístico por cluster
   - **Exportación de asignaciones** a CSV para reportes

### Dataset Sintético: Alfajores

**Variables:**
- `marca`: Marca del alfajor (Tradición, Artisanal, Delicia, Premium, etc.)
- `precio`: Precio en unidades monetarias (54-265)
- `peso_g`: Peso en gramos (24-71)
- `azucar_pct`: Porcentaje de azúcar (18-43%)
- `relleno`: Tipo de relleno (dulce_de_leche, ganache, crema, mousse, fruta, manjar)
- `calificacion`: Calificación del producto (3-5 estrellas)
- `ventas_units`: Unidades vendidas en período (109-260)

**Nota:** Este dataset es completamente ficticio y se generó para propósitos educativos. Es útil para validar pipelines de análisis; para obtener conclusiones comerciales reales, utilizar datos reales de ventas.




