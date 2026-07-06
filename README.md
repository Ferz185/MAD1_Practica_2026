# Métodos para el Análisis de Datos I

## 📊 Descripción del Proyecto

Este repositorio contiene la **parte práctica de la materia "Métodos para el Análisis de Datos I"**, organizando los trabajos prácticos de todas las unidades del curso con una progresión desde conceptos fundamentales hasta técnicas avanzadas de aprendizaje automático.

El proyecto integra teoría y práctica con material educativo estructurado, ejercicios prácticos, datasets reales y proyectos integradores.

## 🎯 Objetivos

- Dominar las técnicas de carga, limpieza y preparación de datos
- Aplicar análisis estadístico y exploratorio a datos reales
- Desarrollar modelos predictivos y de clasificación
- Implementar técnicas de aprendizaje automático supervisado y no supervisado
- Comunicar resultados mediante visualizaciones efectivas

## 📁 Estructura del Repositorio

```
.
├── Unidad 1/                    # Gestión y Preparación de Datos
│   ├── Clases teóricas (PDFs)   # Fuentes, calidad, transformación, APIs
│   ├── U1_practica_python.ipynb # Ejercicios prácticos Python
│   ├── U1_practica_R.Rmd        # Ejercicios prácticos R
│   └── Datasets                 # Conjuntos de datos para práctica
│
├── Unidad 2 y 3/                # Análisis Exploratorio y Regresión
│   ├── Unidad 2: Análisis Exploratorio
│   │   ├── Estadística Descriptiva (Univariada y Bivariada)
│   │   ├── Visualización en Python y R
│   │   ├── Análisis de Distribuciones y Outliers
│   │   └── PCA e Interpretación Visual
│   ├── Unidad 3: Modelos Regresivos
│   │   ├── Regresión Lineal Simple y Múltiple
│   │   ├── Supuestos y Análisis de Residuos
│   │   ├── Selección de Variables
│   │   ├── Regularización (Ridge y Lasso)
│   │   └── Regresión Logística
│   ├── Proyecto Hackathon MAD 2026
│   │   ├── Entregable.ipynb     # Análisis completo
│   │   ├── ordenes_de_compras_municipales-2024.csv
│   │   └── Explorador interactivo de datos
│   └── Notebooks Python y R con ejercicios
│
├── Unidad 4/                    # Aprendizaje Automático Supervisado
│   ├── Árboles de Decisión
│   ├── Random Forest
│   ├── Máquinas de Vectores de Soporte (SVM)
│   ├── K-Nearest Neighbors (KNN)
│   ├── Redes Neuronales
│   └── Métricas de Evaluación y Validación
│
├── Unidad 5/                    # Aprendizaje Automático No Supervisado
│   ├── Clustering (K-means, Jerárquico, etc.)
│   ├── Técnicas de Representación y Dimensionalidad
│   ├── Métodos de Densidad (DBSCAN, LOF)
│   └── Autoencoders
│
└── README.md                    
```

## 📚 Contenido por Unidades

### **Unidad 1: Gestión y Preparación de Datos**
Fundamentos críticos para todo análisis de datos:
- **Fuentes de datos**: Carga desde archivos, bases de datos, APIs web
- **Calidad de datos**: Identificación y tratamiento de valores faltantes, outliers
- **Transformación**: Conversión de tipos, creación de variables derivadas
- **Normalización e Integración**: Estandarización y combinación de datos
- **APIs y Web Scraping**: Extracción de datos de fuentes online
- **Datos Tidy**: Estructura y formato adecuado para análisis

**Material**: Clases teóricas (PDFs), prácticas en Python y R con datasets reales

---

### **Unidad 2: Análisis Exploratorio de Datos (EDA)**
Técnicas estadísticas y visualización:
- **Estadística Descriptiva Univariada**: Medidas de tendencia central, dispersión, forma
- **Estadística Descriptiva Bivariada**: Correlación, covarianza, asociación
- **Distribuciones y Detección de Outliers**: Análisis de distribuciones, métodos de detección
- **Visualización en Python y R**: Gráficos estáticos e interactivos
- **Análisis de Componentes Principales (PCA)**: Reducción dimensional y visualización

**Material**: Notebooks Python, prácticas en R, análisis exploratorio de datos complejos

---

### **Unidad 3: Modelos Regresivos**
Predicción de variables continuas y clasificación:
- **Regresión Lineal Simple**: Fundamentals, ajuste y evaluación
- **Supuestos y Análisis de Residuos**: Validación del modelo
- **Regresión Lineal Múltiple**: Extensión a múltiples variables
- **Multicolinealidad y VIF**: Detección y tratamiento
- **Selección de Variables**: Métodos forward, backward, stepwise
- **Regularización (Ridge y Lasso)**: Control de overfitting
- **Regresión Logística**: Clasificación binaria

**Proyecto Práctico**: Hackathon MAD 2026 - Análisis de órdenes de compra municipal con técnicas EDA y modelado regresivo

**Material**: Notebooks extensos, prácticas en ambos lenguajes

---

### **Unidad 4: Aprendizaje Automático Supervisado**
Algoritmos de predicción y clasificación:
- **Árboles de Decisión**: Particionamiento recursivo, interpretabilidad
- **Random Forest**: Ensambles, importancia de variables
- **Máquinas de Vectores de Soporte (SVM)**: Margen máximo, kernels
- **K-Nearest Neighbors (KNN)**: Clasificación por proximidad
- **Redes Neuronales**: Perceptrones, backpropagation, arquitecturas
- **Métricas de Evaluación**: Accuracy, Precisión, Recall, F1, ROC-AUC
- **Validación Cruzada y Ajuste de Hiperparámetros**

**Material**: 5 notebooks prácticos con implementaciones en Python, teoría completa y aplicaciones

---

### **Unidad 5: Aprendizaje Automático No Supervisado**
Descubrimiento de patrones sin etiquetas:
- **Clustering**: K-means, clustering jerárquico, DBSCAN
- **Técnicas de Representación**: Análisis factorial, t-SNE, UMAP
- **Métodos de Densidad**: DBSCAN, LOF, detección de anomalías
- **Autoencoders**: Redes neuronales para reducción dimensional
- **Interpretación de Resultados**: Validación sin etiquetas

**Material**: 4 notebooks con técnicas no supervisadas y casos de uso reales

---

## 🛠️ Tecnologías Utilizadas

- **Python**: Scikit-learn, Pandas, NumPy, Matplotlib, Plotly, TensorFlow/Keras
- **R**: ggplot2, caret, tidyverse
- **Jupyter Notebooks**: Documentación interactiva
- **Herramientas Complementarias**: APIs, Web Scraping, Visualización interactiva

## 📋 Requisitos

- Python 3.7+ con librerías: pandas, numpy, scikit-learn, matplotlib, plotly, tensorflow
- R 4.0+ con packages: tidyverse, ggplot2, caret
- Jupyter Notebook
- Git para control de versiones

## 👥 Materia

**Métodos para el Análisis de Datos I - 2026**  
Universidad Nacional del Sur
Alumno: Fernando Ezequiel Ramón
Profesor: Jose Bavio

---

**Última actualización**: 2026-07-06
