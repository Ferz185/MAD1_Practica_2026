# Unidad 5: Aprendizaje Automático No Supervisado

## 📚 Descripción

En esta unidad aprenderás técnicas de aprendizaje automático no supervisado, donde los datos NO tienen etiquetas previas. El objetivo es descubrir patrones, estructuras y relaciones inherentes en los datos.

## 🎯 Objetivos

- Identificar y agrupar datos similares sin etiquetas previas
- Reducir dimensionalidad conservando información importante
- Detectar anomalías y valores atípicos
- Comprender técnicas de representación de datos
- Aplicar métodos de densidad para clustering flexible
- Implementar y usar autoencoders

## 📖 Contenido de la Unidad

### **Bloque 1: Clustering**
- `U5_bloque1_clustering.ipynb`
- K-Means: particionamiento en K clusters
- Clustering jerárquico (aglomerativo)
- DBSCAN: clustering basado en densidad
- Selección del número óptimo de clusters
- Evaluación sin etiquetas (silueta, Davies-Bouldin)

### **Bloque 2: Técnicas de Representación**
- `U5_bloque2_representacion.ipynb`
- Análisis Factorial (Factor Analysis)
- t-SNE: visualización de datos de alta dimensión
- UMAP: reducción dimensional preservando estructura
- PCA (repaso de Unidad 2)
- Interpretación de espacios latentes

### **Bloque 3: Métodos de Densidad**
- `U5_bloque3_densidad.ipynb`
- DBSCAN (profundización)
- LOF (Local Outlier Factor)
- Isolation Forest para detección de anomalías
- Aplicaciones en calidad de datos
- Detección de fraude y valores atípicos

### **Bloque 4: Autoencoders**
- `U5_bloque4_autoencoders.ipynb`
- Arquitectura de autoencoders
- Aprendizaje de representaciones
- Reducción dimensional con redes neuronales
- Anomaly detection con autoencoders
- Variational Autoencoders (VAE) conceptos básicos

### **Proyecto Integrador: Análisis de Chocolate**
- `Unidad5_chocolate.ipynb`
- Aplicación de técnicas no supervisadas a dataset real
- Clustering de productos
- Análisis de características latentes
- Recomendaciones basadas en clustering

## 🛠️ Herramientas y Librerías

```python
import sklearn
from sklearn.cluster import KMeans, AgglomerativeClustering, DBSCAN
from sklearn.decomposition import FactorAnalysis, PCA
from sklearn.manifold import TSNE
from sklearn.neighbors import LocalOutlierFactor
from sklearn.ensemble import IsolationForest
import umap
import tensorflow as tf
from tensorflow import keras
from sklearn.metrics import silhouette_score, davies_bouldin_score
```

## 📋 Flujo de Trabajo Recomendado

1. **Preparación**: Cargar y normalizar datos (crítico en no supervisado)
2. **EDA**: Exploración inicial de patrones
3. **Seleccionar técnica**: Elegir según objetivo
4. **Aplicar algoritmo**: Entrenar modelo
5. **Evaluación**: Usar métricas sin etiquetas
6. **Interpretación**: Analizar clusters/patrones encontrados
7. **Validación**: Verificar estabilidad de resultados
8. **Visualización**: Representar en 2D/3D si es posible

## 📊 Ejemplo Básico K-Means

```python
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score

# Normalizar (IMPORTANTE en no supervisado)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Entrenar K-Means
kmeans = KMeans(n_clusters=3, random_state=42)
labels = kmeans.fit_predict(X_scaled)

# Evaluar
silhouette_avg = silhouette_score(X_scaled, labels)
print(f"Silhouette Score: {silhouette_avg:.3f}")

# Visualizar
plt.scatter(X_scaled[:, 0], X_scaled[:, 1], c=labels, cmap='viridis')
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], 
            c='red', marker='X', s=200)
plt.show()
```

## ✅ Actividades Requeridas

Para completar esta unidad debes:

1. **Ejecutar todos los notebooks** en orden secuencial
2. **Comprender diferencias** entre los algoritmos
3. **Elegir número de clusters** apropiado (codo, silhueta)
4. **Aplicar normalización** antes de clustering
5. **Interpretar resultados**: ¿qué representan los clusters?
6. **Visualizar**: Usar t-SNE o UMAP para entender patrones
7. **Detectar anomalías** usando métodos de densidad
8. **Implementar autoencoder** básico
9. **Resolver proyecto chocolate**: Análisis completo con recomendaciones

## 📊 Comparación de Técnicas de Clustering

| Algoritmo | Escalabilidad | Densidad | Forma | Parámetros | Mejor para |
|-----------|---------------|----------|-------|-----------|-----------|
| K-Means | Alta | Esférica | Esférica | K | Clusters bien separados |
| Jerárquico | Media | Variable | Flexible | Distancia | Análisis exploratorio |
| DBSCAN | Media | Variable | Arbitraria | eps, min_pts | Clusters irregulares |
| LOF | Baja | Densidad local | Cualquier | K | Anomalías |
| Autoencoders | Media | Flexible | Flexible | Arquitectura | Datos complejos |

## 🔍 Métodos de Evaluación Sin Etiquetas

- **Silhouette Score**: Mide cohesión (más alto es mejor, -1 a 1)
- **Davies-Bouldin Index**: Mide separación (más bajo es mejor)
- **Calinski-Harabasz Index**: Relación cohesión/dispersión (más alto es mejor)
- **Inercia (Within-cluster sum of squares)**: Solo para K-Means
- **Estabilidad**: Cambiar datos/parámetros y comparar resultados

## 🎨 Técnicas de Visualización

```python
from sklearn.manifold import TSNE
import umap

# t-SNE (bueno para estructura local)
tsne = TSNE(n_components=2, perplexity=30)
X_tsne = tsne.fit_transform(X_scaled)

# UMAP (más rápido, preserva estructura global)
reducer = umap.UMAP()
X_umap = reducer.fit_transform(X_scaled)

# Visualizar
plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
plt.scatter(X_tsne[:, 0], X_tsne[:, 1], c=labels, cmap='viridis')
plt.title('t-SNE')

plt.subplot(1, 2, 2)
plt.scatter(X_umap[:, 0], X_umap[:, 1], c=labels, cmap='viridis')
plt.title('UMAP')
plt.show()
```

## 📋 Checklist de Finalización

Al completar esta unidad deberías:

- ✅ Entender cuándo usar clustering vs dimensionalidad
- ✅ Elegir algoritmo apropiado según datos
- ✅ Normalizar datos correctamente
- ✅ Determinar número óptimo de clusters
- ✅ Evaluar calidad sin etiquetas
- ✅ Interpretar y visualizar resultados
- ✅ Detectar anomalías
- ✅ Implementar autoencoders básicos
- ✅ Completar proyecto integrador (chocolate)
- ✅ Documentar todo en notebooks

## 🚀 Proyecto Final: Análisis de Chocolate (OBLIGATORIO)

El notebook `Unidad5_chocolate.ipynb` contiene un análisis completo que debes:

1. **Ejecutar y entender** cada celda
2. **Modificar parámetros** para mejores resultados
3. **Agregar visualizaciones** adicionales (t-SNE, UMAP)
4. **Escribir conclusiones**: ¿Qué clusters encontraste?
5. **Hacer recomendaciones**: ¿Cómo usar estos clusters?
6. **Proponer mejoras**: ¿Qué harías diferente?

### Preguntas a Responder en el Proyecto

- ¿Cuántos grupos naturales existen en los datos?
- ¿Qué características definen cada grupo?
- ¿Hay anomalías o productos atípicos?
- ¿Cómo cambiarían los clusters con diferentes parámetros?
- ¿Cuál es la utilidad práctica de estos clusters?

## 📚 Recursos Adicionales

- [Scikit-learn Clustering](https://scikit-learn.org/stable/modules/clustering.html)
- [UMAP Documentation](https://umap-learn.readthedocs.io/)
- [Autoencoder Guides](https://blog.keras.io/building-autoencoders-in-keras.html)
- Lecturas: PDFs de teoría de Unidad 5

---

**Última actualización**: 2026-07-06
